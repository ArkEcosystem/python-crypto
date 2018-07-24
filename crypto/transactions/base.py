from hashlib import sha256
from struct import pack

from base58 import b58decode_check

from binary.hex.writer import write_high
from binary.unsigned_integer.writer import write_bit32, write_bit64, write_bit8

from crypto.identity.keys import public_key_from_passphrase
from crypto.message import sign_message, verify_message
from crypto.slot import get_time


TRANSACTION_ATTRIBUTES = {
    'amount': 0,
    'asset': dict,
    'fee': None,
    'id': None,
    'network': None,
    'recipient_id': None,
    'second_signature': None,
    'sender_public_key': None,
    'signature': None,
    'signatures': None,
    'sign_signature': None,
    'timestamp': get_time,
    'type': None,
    'vendor_field': None,
    'version': None,
}


class Transaction(object):

    def __init__(self, *args, **kwargs):
        for attribute, attribute_value in TRANSACTION_ATTRIBUTES.items():
            if callable(attribute_value):
                attribute_value = attribute_value()
            elif attribute == 'type' and not attribute_value:
                attribute_value = self.get_type()
            setattr(self, attribute, attribute_value)

    def get_type(self):
        """Gets the transaction type from a child transaction or set it to None

        Returns:
            str: transaction type
        """
        return getattr(self, 'transaction_type', None)

    def get_id(self):
        """Convert the byte representation to a unique identifier

        Returns:
            str:
        """
        return sha256(self.to_bytes(False, False)).hexdigest()

    def to_dict(self):
        """Convert the transaction into a dictionary representation

        Returns:
            dict:
        """
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
        """Convert the transaction to its byte representation

        Args:
            skip_signature (bool, optional): do you want to skip the signature
            skip_second_signature (bool, optional): do you want to skip the 2nd signature

        Returns:
            bytes: bytes representation of the transaction
        """
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

    def parse_signatures(self, serialized, start_offset):
        """Parse the signature, second signature and multi signatures

        Args:
            serialized (str): parses a given serialized string
            start_offset (int):

        Returns:
            None: methods returns nothing
        """
        self.signature = serialized[start_offset:]
        multi_signature_offset = 0

        if not len(self.signature):
            self.signature = None
            return

        signature_length = int(self.signature[2:4], base=16) + 2
        self.signature = serialized[start_offset: start_offset + (signature_length * 2)]
        multi_signature_offset += signature_length * 2
        self.sign_signature = serialized[start_offset + (signature_length * 2):]

        if not self.sign_signature:
            self.sign_signature = None
        elif 'ff' == self.sign_signature[:2]:
            self.sign_signature = None
        else:
            second_signature_length = int(self.sign_signature[2:4], base=16)
            self.sign_signature = self.sign_signature[:second_signature_length * 2]
            multi_signature_offset += second_signature_length * 2

        signatures = serialized[:start_offset + multi_signature_offset]

        if not signatures:
            return

        if 'ff' != signatures[:2]:
            return

        signatures = signatures[2:]
        self.signatures = []

        while True:
            mlength = int(signatures[2:4], base=16)
            if mlength > 0:
                self.signatures.append(signatures[:(mlength + 2) * 2])
            else:
                break

            signatures = signatures[(mlength + 2) * 2:]
            if not signatures:
                break

    def sign(self, passphrase):
        """Sign the transaction using the given passphrase

        Args:
            passphrase (str): passphrase associated with the account sending this transaction
        """
        self.sender_public_key = public_key_from_passphrase(passphrase)
        transaction = sha256(self.to_bytes()).digest()
        message = sign_message(transaction, passphrase)
        self.signature = message['signature']

    def second_sign(self, passphrase):
        """Sign the transaction using the given second passphrase

        Args:
            passphrase (str): 2nd passphrase associated with the account sending this transaction
        """
        transaction = sha256(self.to_bytes()).digest()
        message = sign_message(transaction, passphrase)
        self.sign_signature = message['signature']

    def verify(self):
        """Verify the transaction. Method will raise an exception if invalid, if it's valid nothing
        will happen.
        """
        transaction = sha256(self.to_bytes()).digest()
        verify_message(transaction, self.sender_public_key, self.signature)

    def second_verify(self, passphrase):
        """Verify the transaction using the 2nd passphrase

        Args:
            passphrase (str): 2nd passphrase associated with the account sending this transaction
        """
        transaction = sha256(self.to_bytes()).digest()
        verify_message(transaction, self.sender_public_key, self.signSignature)

    def handle_transaction_type(self, bytes_data):
        """Each child transaction needs to have this method defined

        Args:
            bytes_data (bytes): input the bytes data to which you want to append new bytes

        Raises:
            NotImplementedError: raised only if the child transaction doesn't implement this
            required method
        """
        raise NotImplementedError

    def _handle_signature(self, bytes_data, skip_signature, skip_second_signature):
        """Internal method, used to handle the signature

        Args:
            bytes_data (bytes): input the bytes data to which you want to append new bytes from
            signature
            skip_signature (bool): whether you want to skip it or not
            skip_second_signature (bool): whether you want to skip it or not

        Returns:
            TYPE: Description
        """
        if not skip_signature and self.signature:
            bytes_data += write_high(self.signature)
        if not skip_second_signature and self.sign_signature:
            bytes_data += write_high(self.sign_signature)
        return bytes_data
