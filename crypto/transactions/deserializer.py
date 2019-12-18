import inspect
from binascii import hexlify, unhexlify
from hashlib import sha256
from importlib import import_module

from binary.unsigned_integer.reader import read_bit8, read_bit16, read_bit32, read_bit64

from crypto.constants import TRANSACTION_TYPES
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
        transaction.network = read_bit8(self.serialized, offset=2)
        transaction.typeGroup = read_bit32(self.serialized, offset=3)
        transaction.type = read_bit16(self.serialized, offset=7)
        transaction.nonce = read_bit64(self.serialized, offset=9)
        transaction.senderPublicKey = hexlify(self.serialized)[34:66+34].decode()
        transaction.fee = read_bit64(self.serialized, offset=50)

        vendor_field_length = read_bit8(self.serialized, offset=58)
        if vendor_field_length > 0:
            vendor_field_offset = (58 + 8) * 2
            vendorField_take = vendor_field_length * 2
            transaction.vendorFieldHex = hexlify(
                self.serialized
            )[vendor_field_offset:vendorField_take]

        asset_offset = (58 + 1) * 2 + vendor_field_length * 2

        handled_transaction = self._handle_transaction_type(asset_offset, transaction)
        transaction.amount = handled_transaction.amount
        transaction.version = handled_transaction.version
        if transaction.version == 2:
            transaction = self._handle_version_two(transaction)
        else:
            raise Exception('should this ever happen?')

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

    def _handle_version_two(self, transaction):
        """Handle deserialization for version two

        Args:
            transaction (object): Transaction resource object

        Returns:
            object: Transaction resource object of currently deserialized data
        """

        transaction.id = sha256(unhexlify(transaction.serialize(False, True, False))).hexdigest()

        return transaction
