import json
from binascii import hexlify
from hashlib import sha256
from struct import pack

from base58 import b58decode_check

from binary.hex.writer import write_high
from binary.unsigned_integer.writer import write_bit32, write_bit64, write_bit8

from crypto.constants import (
    TRANSACTION_DELEGATE_REGISTRATION, TRANSACTION_MULTI_SIGNATURE_REGISTRATION,
    TRANSACTION_SECOND_SIGNATURE_REGISTRATION, TRANSACTION_VOTE
)
from crypto.deserializer import Deserializer
from crypto.message import verify_message
from crypto.serializer import Serializer
from crypto.slot import get_time


TRANSACTION_ATTRIBUTES = {
    'amount': 0,
    'asset': dict,
    'fee': None,
    'id': None,
    'network': None,
    'recipientId': None,
    'secondSignature': None,
    'senderPublicKey': None,
    'signature': None,
    'signatures': None,
    'signSignature': None,
    'timestamp': get_time,
    'type': None,
    'vendorField': None,
    'vendorFieldHex': None,
    'version': None,
}


class Transaction(object):

    def __init__(self, *args, **kwargs):
        for attribute, attribute_value in TRANSACTION_ATTRIBUTES.items():
            if callable(attribute_value):
                attribute_value = attribute_value()
            if attribute in kwargs:
                attribute_value = kwargs[attribute]
            setattr(self, attribute, attribute_value)

    def get_id(self):
        """Convert the byte representation to a unique identifier

        Returns:
            str:
        """
        return sha256(self.to_bytes(False, False)).hexdigest()

    def to_dict(self):
        """Convert the transaction into a dictionary representation

        Returns:
            dict: only includes values that are set
        """
        data = {}
        for key in TRANSACTION_ATTRIBUTES.keys():
            attribute = getattr(self, key, None)
            if attribute is None:
                continue
            data[key] = attribute
        return data

    def to_json(self):
        data = self.to_dict()
        return json.loads(data)

    def to_bytes(self, skip_signature=True, skip_secondSignature=True):
        """Convert the transaction to its byte representation

        Args:
            skip_signature (bool, optional): do you want to skip the signature
            skip_secondSignature (bool, optional): do you want to skip the 2nd signature

        Returns:
            bytes: bytes representation of the transaction
        """
        bytes_data = bytes()
        bytes_data += write_bit8(self.type)
        bytes_data += write_bit32(self.timestamp)
        bytes_data += write_high(self.senderPublicKey)

        if self.recipientId:
            bytes_data += b58decode_check(self.recipientId)
        else:
            bytes_data += pack('21x')

        if self.vendorField and len(self.vendorField) < 64:
            bytes_data += self.vendorField
            bytes_data += pack('{}x'.format(64 - len(self.vendorField)))
        else:
            bytes_data += pack('64x')

        bytes_data += write_bit64(self.amount)
        bytes_data += write_bit64(self.fee)

        bytes_data = self._handle_transaction_type(bytes_data)
        bytes_data = self._handle_signature(bytes_data, skip_signature, skip_secondSignature)

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
        self.signSignature = serialized[start_offset + (signature_length * 2):]

        if not self.signSignature:
            self.signSignature = None
        elif 'ff' == self.signSignature[:2]:
            self.signSignature = None
        else:
            secondSignature_length = int(self.signSignature[2:4], base=16)
            self.signSignature = self.signSignature[:secondSignature_length * 2]
            multi_signature_offset += secondSignature_length * 2

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

    def serialize(self):
        data = self.to_dict()
        return Serializer(data).serialize()

    def deserialize(self, serialized):
        return Deserializer(serialized).deserialize()

    def verify(self):
        """Verify the transaction. Method will raise an exception if invalid, if it's valid nothing
        will happen.
        """
        transaction = sha256(self.to_bytes()).digest()
        verify_message(transaction, self.senderPublicKey, self.signature)

    def second_verify(self, passphrase):
        """Verify the transaction using the 2nd passphrase

        Args:
            passphrase (str): 2nd passphrase associated with the account sending this transaction
        """
        transaction = sha256(self.to_bytes()).digest()
        verify_message(transaction, self.senderPublicKey, self.signSignature)

    def _handle_transaction_type(self, bytes_data):
        """Handled each transaction type differently

        Args:
            bytes_data (bytes): input the bytes data to which you want to append new bytes

        Raises:
            NotImplementedError: raised only if the child transaction doesn't implement this
            required method
        """
        if self.type == TRANSACTION_SECOND_SIGNATURE_REGISTRATION:
            public_key = self.asset['signature']['publicKey']
            bytes_data += hexlify(public_key)
        elif self.type == TRANSACTION_DELEGATE_REGISTRATION:
            bytes_data += self.asset['delegate']['username']
        elif self.type == TRANSACTION_VOTE:
            bytes_data += ''.join(self.asset['votes']).encode()
        elif self.type == TRANSACTION_MULTI_SIGNATURE_REGISTRATION:
            bytes_data += write_bit8(self.asset['multisignature']['min'])
            bytes_data += write_bit8(self.asset['multisignature']['lifetime'])
            bytes_data += ''.join(self.asset['multisignature']['keysgroup']).encode()
        return bytes_data

    def _handle_signature(self, bytes_data, skip_signature, skip_secondSignature):
        """Internal method, used to handle the signature

        Args:
            bytes_data (bytes): input the bytes data to which you want to append new bytes from
            signature
            skip_signature (bool): whether you want to skip it or not
            skip_secondSignature (bool): whether you want to skip it or not

        Returns:
            bytes: bytes string
        """
        if not skip_signature and self.signature:
            bytes_data += write_high(self.signature)
        if not skip_secondSignature and self.signSignature:
            bytes_data += write_high(self.signSignature)
        return bytes_data
