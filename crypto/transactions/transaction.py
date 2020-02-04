import json
from binascii import unhexlify
from hashlib import sha256

from binary.hex.writer import write_high
from binary.unsigned_integer.writer import write_bit8

from crypto.constants import (
    TRANSACTION_DELEGATE_REGISTRATION, TRANSACTION_MULTI_SIGNATURE_REGISTRATION,
    TRANSACTION_SECOND_SIGNATURE_REGISTRATION, TRANSACTION_VOTE
)
from crypto.exceptions import ArkInvalidTransaction
from crypto.schnorr import schnorr
from crypto.transactions.deserializer import Deserializer
from crypto.transactions.serializer import Serializer

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
    'nonce': None,
    'type': None,
    'typeGroup': None,
    'vendorField': None,
    'vendorFieldHex': None,
    'version': None,
    'lockTransactionId': None,
    'lockSecret': None,
    'expiration': None
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
        return sha256(self.to_bytes(skip_signature=False, skip_second_signature=False, skip_multi_signature=False)).hexdigest()

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

    def to_bytes(self, skip_signature=True, skip_second_signature=True, skip_multi_signature=True):
        """Convert the transaction to its byte representation

        Args:
            skip_signature (bool, optional): do you want to skip the signature
            skip_second_signature (bool, optional): do you want to skip the 2nd signature
            skip_multi_signature (bool, optional): do you want to skip multi signature

        Returns:
            bytes: bytes representation of the transaction
        """
        return Serializer(self.to_dict()).serialize(skip_signature=skip_signature,
                                                    skip_second_signature=skip_second_signature,
                                                    skip_multi_signature=skip_multi_signature,
                                                    raw=True)

    def parse_signatures(self, serialized, start_offset):
        """Parse the signature, second signature and multi signatures

        Args:
            serialized (str): parses a given serialized string
            start_offset (int):

        Returns:
            None: methods returns nothing
        """

        signature_end_offset = start_offset + (64 * 2)

        if len(serialized) - signature_end_offset % 65 != 0:
            self.signature = serialized[start_offset:signature_end_offset]

        second_signature_end_offset = signature_end_offset + (64 * 2)
        if len(serialized) - signature_end_offset > 0 and (len(serialized) - signature_end_offset) % 64 == 0:
            self.signSignature = serialized[signature_end_offset:second_signature_end_offset]

        if len(serialized) - second_signature_end_offset > 0 and (len(serialized) - signature_end_offset) % 65 == 0:
            multi_sig_part = serialized[signature_end_offset:]
            index = 0
            index_size = 2
            signature_size = 128

            while index != len(multi_sig_part):
                signature_index = multi_sig_part[index:index + index_size]
                signature = multi_sig_part[index + index_size:index + index_size + signature_size]
                index += index_size + signature_size
                signature_formatted = signature_index + signature
                self.signatures.append(signature_formatted)

        return

    def serialize(self, skip_signature=True, skip_second_signature=True, skip_multi_signature=True):
        """Perform AIP11 compliant serialization.

        Args:
            skip_signature (bool, optional): do you want to skip the signature
            skip_second_signature (bool, optional): do you want to skip the 2nd signature
            skip_multi_signature (bool, optional): do you want to skip multi signature

        Returns:
            str: Serialized string
        """
        data = self.to_dict()
        return Serializer(data).serialize(skip_signature, skip_second_signature, skip_multi_signature)

    def deserialize(self, serialized):
        """Perform AIP11 compliant deserialization.

        Args:
            serialized (str): parses a given serialized string

        Returns:
            crypto.transactions.transaction.Transaction: Transaction
        """
        return Deserializer(serialized).deserialize()

    def verify_schnorr(self):
        """Verify the transaction. Method will raise an exception if invalid, if it's valid it will
        returns True
        """
        is_valid = schnorr.b410_schnorr_verify(self.to_bytes(), self.senderPublicKey, self.signature)

        if not is_valid:
            raise ArkInvalidTransaction('Transaction could not be verified')

        return is_valid

    def verify_schnorr_secondsig(self, secondPublicKey):
        """Verify the transaction. Method will raise an exception if invalid, if it's valid it will
        returns True
        """
        is_valid = schnorr.b410_schnorr_verify(self.to_bytes(False, True), secondPublicKey, self.signSignature)
        
        if not is_valid:
            raise ArkInvalidTransaction('Transaction could not be verified')
    
    def verify_schnorr_multisig(self):
        """Verify the multisignatures transaction. Method will raise an exception if invalid, it will
        returns True
        """
        is_valid = schnorr.b410_schnorr_verify(self.to_bytes(True, True, False), self.senderPublicKey, self.signature)

        if not is_valid:
            raise ArkInvalidTransaction('Transaction could not be verified')

        return is_valid

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
            bytes_data += ''.join(self.asset['multiSignature']['publicKeys']).encode()

        return bytes_data

    def _handle_signature(self, bytes_data, skip_signature, skip_second_signature, skip_multi_signature):
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
        if not skip_multi_signature and self.signatures:
            bytes_data += write_high(self.signatures)
        return bytes_data
