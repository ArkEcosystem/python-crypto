import json
from binascii import unhexlify
from hashlib import sha256
from struct import pack

from base58 import b58decode_check

from binary.hex.writer import write_high
from binary.unsigned_integer.writer import write_bit32, write_bit64, write_bit8

from crypto.constants import (
    TRANSACTION_DELEGATE_REGISTRATION, TRANSACTION_MULTI_SIGNATURE_REGISTRATION,
    TRANSACTION_SECOND_SIGNATURE_REGISTRATION, TRANSACTION_VOTE, TRANSACTION_MULTI_PAYMENT
)
from crypto.exceptions import ArkInvalidTransaction
from crypto.transactions.deserializer import Deserializer
from crypto.transactions.serializer import Serializer
from crypto.utils.message import Message


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
    'nonce': None, # set it properly
    'type': None,
    'typeGroup': None, # set it properly
    'vendorField': None,
    'vendorFieldHex': None,
    'version': None, # set it properly
    'lockTransactionId': None,
    'lockSecret': None
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
        return sha256(self.to_bytes(skip_signature=False, skip_second_signature=False)).hexdigest()

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
            # todo: get rid of the bytes check and handle this outside of the to_dict function
            data[key] = attribute.decode() if isinstance(attribute, bytes) else attribute
        return data

    def to_json(self):
        data = self.to_dict()
        return json.dumps(data)

    def to_bytes(self, skip_signature=True, skip_second_signature=True):
        """Convert the transaction to its byte representation

        Args:
            skip_signature (bool, optional): do you want to skip the signature
            skip_second_signature (bool, optional): do you want to skip the 2nd signature

        Returns:
            bytes: bytes representation of the transaction
        """
        return Serializer(self.to_dict()).serialize(skip_signature=skip_signature, skip_second_signature=skip_second_signature, raw=True)

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

    def serialize(self, skip_signature=True, skip_second_signature=True):
        data = self.to_dict()
        return Serializer(data).serialize(skip_signature, skip_second_signature)

    def deserialize(self, serialized):
        return Deserializer(serialized).deserialize()

    def verify(self):
        """Verify the transaction. Method will raise an exception if invalid, if it's valid nothing
        will happen.
        """
        transaction = self.to_bytes()
        message = Message(transaction, self.signature, self.senderPublicKey)
        is_valid = message.verify()
        if not is_valid:
            raise ArkInvalidTransaction('Transaction could not be verified')

    def second_verify(self, passphrase):
        """Verify the transaction using the 2nd passphrase

        Args:
            passphrase (str): 2nd passphrase associated with the account sending this transaction
        """
        transaction = sha256(self.to_bytes()).digest()
        message = Message(transaction, self.signSignature, self.senderPublicKey)
        is_valid = message.verify()
        if not is_valid:
            raise ArkInvalidTransaction('Transaction could not be verified')

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
            bytes_data += unhexlify(public_key)
        elif self.type == TRANSACTION_DELEGATE_REGISTRATION:
            bytes_data += self.asset['delegate']['username'].encode()
        elif self.type == TRANSACTION_VOTE:
            bytes_data += ''.join(self.asset['votes']).encode()
        elif self.type == TRANSACTION_MULTI_SIGNATURE_REGISTRATION:
            bytes_data += write_bit8(self.asset['multiSignature']['min'])
            bytes_data += write_bit8(self.asset['multiSignature']['lifetime'])
            bytes_data += ''.join(self.asset['multiSignature']['publicKeys']).encode()
        #elif self.type == TRANSACTION_MULTI_PAYMENT: # Not really sure here
        #    bytes_data += self.asset['payments'].encode()
        return bytes_data

    def _handle_signature(self, bytes_data, skip_signature, skip_second_signature):
        """Internal method, used to handle the signature

        Args:
            bytes_data (bytes): input the bytes data to which you want to append new bytes from
            signature
            skip_signature (bool): whether you want to skip it or not
            skip_second_signature (bool): whether you want to skip it or not

        Returns:
            bytes: bytes string
        """
        if not skip_signature and self.signature:
            bytes_data += write_high(self.signature)
        if not skip_second_signature and self.signSignature:
            bytes_data += write_high(self.signSignature)
        return bytes_data
