from binascii import hexlify
from hashlib import sha256
from struct import pack

from base58 import b58decode_check

from binary.hex.writer import write_high
from binary.unsigned_integer.writer import write_bit32, write_bit64, write_bit8

from crypto.identity.keys import public_key_from_secret
from crypto.message import sign_message, verify_message
from crypto.slot import get_time


class BaseTransaction(object):

    def __init__(self):
        self.recipient_id = None
        self.amount = 0
        self.type = self.get_type()
        self.fee = None
        self.vendor_field = None
        self.timestamp = get_time()
        self.sender_public_key = None
        self.signature = None
        self.sign_signature = None
        self.id = None
        self.asset = {}

    def get_type(self):
        return self.transaction_type

    def get_id(self):
        return sha256(hexlify(self.to_bytes(False, False)))

    def to_dict(self):
        data = {
            'recipientId': self.recipient_id,
            'type': self.type,
            'amount': self.amount,
            'fee': self.fee,
            'vendorField': self.vendor_field,
            'timestamp': self.timestamp,
            'senderPublicKey': self.sender_public_key,
            'signature': self.signature,
            'signSignature': self.sign_signature,
            'id': self.id,
            'asset': self.asset,
        }
        return data

    def to_bytes(self, skip_signature=True, skip_second_signature=True):
        bytes_data = bytes()
        bytes_data += write_bit8(self.type)
        bytes_data += write_bit32(self.timestamp)
        bytes_data += write_high(self.sender_public_key)

        if self.recipient_id:
            bytes_data += b58decode_check(self.recipient_id)
        else:
            bytes_data += pack('21x')

        if self.vendor_field and len(self.vendor_field) < 64:
            bytes_data += self.vendor_field
            bytes_data += pack('{}x'.format(64 - len(self.vendor_field)))
        else:
            bytes_data += pack('64x')

        bytes_data += write_bit64(self.amount)
        bytes_data += write_bit64(self.fee)

        bytes_data = self.handle_transaction_type(bytes_data)
        bytes_data = self._handle_signature(bytes_data, skip_signature, skip_second_signature)

        return bytes_data

    def parse_signatures(self):
        pass  # todo

    def sign(self, passphrase):
        self.sender_public_key = public_key_from_secret(passphrase)
        transaction = sha256(self.to_bytes()).digest()
        message = sign_message(transaction, passphrase)
        self.signature = message['signature']

    def second_sign(self, passphrase):
        transaction = sha256(self.to_bytes()).digest()
        message = sign_message(transaction, passphrase)
        self.sign_signature = message['signature']

    def verify(self):
        transaction = sha256(self.to_bytes()).digest()
        verify_message(transaction, self.sender_public_key, self.signature)

    def second_verify(self, passphrase):
        transaction = sha256(self.to_bytes()).digest()
        verify_message(transaction, self.sender_public_key, self.signSignature)

    def handle_transaction_type(self, bytes_data):
        raise NotImplementedError

    def _handle_signature(self, bytes_data, skip_signature, skip_second_signature):
        if not skip_signature and self.signature:
            bytes_data += write_high(self.signature)
        if not skip_second_signature and self.sign_signature:
            bytes_data += write_high(self.sign_signature)
        return bytes_data
