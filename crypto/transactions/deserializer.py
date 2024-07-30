import inspect
from binascii import hexlify, unhexlify
from importlib import import_module
from typing import Union

from binary.unsigned_integer.reader import read_bit8, read_bit16, read_bit32, read_bit64

from crypto.constants import TRANSACTION_TYPES
from crypto.transactions.deserializers.base import BaseDeserializer
from crypto.transactions.transaction import Transaction

class Deserializer(object):
    serialized: bytes

    def __init__(self, serialized: Union[bytes, str]):
        self.serialized = unhexlify(serialized)

    def deserialize(self) -> Transaction:
        """Deserialize transaction

        Returns:
            Transaction: returns transaction object
        """

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
        transaction.id = transaction.get_id()

        return transaction

    def _handle_transaction_type(self, asset_offset: int, transaction):
        """Handle deserialization for a given transaction type

        Args:
            asset_offset (int):
            transaction (Transaction): Transaction resource object

        Returns:
            Transaction: Transaction object of currently deserialized data
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
