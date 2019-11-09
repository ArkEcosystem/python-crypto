import inspect
from binascii import hexlify, unhexlify
from hashlib import sha256
from importlib import import_module

from binary.unsigned_integer.reader import read_bit32, read_bit64, read_bit8, read_bit16

from crypto.constants import (
    TRANSACTION_MULTI_SIGNATURE_REGISTRATION, TRANSACTION_SECOND_SIGNATURE_REGISTRATION,
    TRANSACTION_TYPES, TRANSACTION_VOTE
)
from crypto.identity.address import address_from_public_key
from crypto.transactions.deserializers.base import BaseDeserializer


class Deserializer(object):

    serialized = None

    def __init__(self, serialized):
        self.serialized = unhexlify(serialized)

    def deserialize(self):
        """Deserialize transaction

        Returns:
            object: returns Transaction resource object
        """
        # circular import with transaction.py :( - I'm thinking of just returning a dict here
        # which then needs to be passed to a Transaction object, instead of returning a Transaction
        # object
        from crypto.transactions.transaction import Transaction

        transaction = Transaction()
        transaction.version = read_bit8(self.serialized, offset=1)
        print(transaction.version)
        transaction.network = read_bit8(self.serialized, offset=2)
        print(transaction.network)
        transaction.typeGroup = read_bit32(self.serialized, offset=3)
        print(transaction.typeGroup)
        transaction.type = read_bit16(self.serialized, offset=7)
        print(transaction.type)
        transaction.nonce = read_bit64(self.serialized, offset=9)
        print(transaction.nonce)
        transaction.senderPublicKey = hexlify(self.serialized)[34:66+34].decode()
        print(transaction.senderPublicKey)
        transaction.fee = read_bit64(self.serialized, offset=50)

        vendor_field_length = read_bit8(self.serialized, offset=58)
        if vendor_field_length > 0:
            vendor_field_offset = (58 + 8) * 2
            vendorField_take = vendor_field_length * 2
            transaction.vendorFieldHex = hexlify(
                self.serialized
            )[vendor_field_offset:vendorField_take]

        asset_offset = (58 + 1) * 2 + vendor_field_length * 2

        print(transaction.to_dict())

        handled_transaction = self._handle_transaction_type(asset_offset, transaction)
        transaction.amount = handled_transaction.amount
        transaction.version = handled_transaction.version
        print(transaction.to_dict())
        print('before version check')
        if transaction.version == 1:
            transaction = self._handle_version_one(transaction)
        elif transaction.version == 2:
            transaction = self._handle_version_two(transaction)
        else:
            raise Exception('should this ever happen?')  # todo: do we need this?

        print('after version check')
        print(transaction)
        return transaction

    def _handle_transaction_type(self, asset_offset, transaction):
        """Handle deserialization for a given transaction type

        Args:
            asset_offset (int):
            transaction (object): Transaction resource object

        Returns:
            object: Transaction resource object of currently deserialized data
        """
        deserializer_name = TRANSACTION_TYPES[transaction.type]
        module = import_module('crypto.transactions.deserializers.{}'.format(deserializer_name))
        for attr in dir(module):
            # If attr name is `BaseDeserializer`, skip it as it's a class and also has a
            # subclass of BaseDeserializer
            if attr == 'BaseDeserializer':
                continue

            attribute = getattr(module, attr)
            if inspect.isclass(attribute) and issubclass(attribute, BaseDeserializer):
                # this attribute is actually a specific deserializer that we want to use
                deserializer = attribute
                break
        return deserializer(self.serialized, asset_offset, transaction).deserialize()

    def _handle_version_one(self, transaction):
        """Handle deserialization for version one

        Args:
            transaction (object): Transaction resource object

        Returns:
            object: Transaction resource object of currently deserialized data
        """
        if transaction.secondSignature:
            transaction.secondSignature = transaction.secondSignature

        if transaction.type is TRANSACTION_VOTE:
            transaction.recipientId = address_from_public_key(
                transaction.senderPublicKey, transaction.network
            )

        if transaction.type is TRANSACTION_MULTI_SIGNATURE_REGISTRATION:
            transaction.asset['multisignature']['keysgroup'] = [
                '+{}'.format(key) for key in transaction.asset['multisignature']['keysgroup']
            ]

        if transaction.vendorFieldHex:
            transaction.vendorField = unhexlify(transaction.vendorFieldHex)

        if not transaction.id:
            transaction.id = transaction.get_id()

        if transaction.type is TRANSACTION_SECOND_SIGNATURE_REGISTRATION:
            transaction.recipientId = address_from_public_key(
                transaction.senderPublicKey, transaction.network
            )

        if transaction.type is TRANSACTION_MULTI_SIGNATURE_REGISTRATION:
            transaction.recipientId = address_from_public_key(
                transaction.senderPublicKey, transaction.network
            )

        return transaction

    def _handle_version_two(self, transaction):
        """Handle deserialization for version two

        Args:
            transaction (object): Transaction resource object

        Returns:
            object: Transaction resource object of currently deserialized data
        """
        transaction.id = sha256(unhexlify(transaction.serialize(False, True))).hexdigest()  # todo serialize
        return transaction
