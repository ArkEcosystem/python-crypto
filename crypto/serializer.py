import inspect
from binascii import unhexlify
from importlib import import_module

from binary.hex.writer import write_high, write_low
from binary.unsigned_integer.writer import write_bit32, write_bit64, write_bit8

from crypto.exceptions import SerializerException
from crypto.serializers.base import BaseSerializer


class Serializer(object):

    serializers = {
        0: 'transfer',
        1: 'second_signature_registration',
        2: 'delegate_registration',
        3: 'vote',
        4: 'multi_signature_registration',
        5: 'ipfs',
        6: 'timelock_transfer',
        7: 'multi_payment',
        8: 'delegate_resignation',
    }
    transaction = None

    def __init__(self, transaction):
        if not transaction:
            raise SerializerException('No transaction data provided')
        self.transaction = transaction

    def serialize(self):
        """Perform AIP11 compliant serialization

        Returns:
            bytes: bytes string
        """
        bytes_data = bytes()
        bytes_data += write_bit8(0xff)
        bytes_data += write_low(self.transaction.get('version') or 0x01)
        bytes_data += write_bit8(self.transaction.get('network') or 1337)  # todo:
        bytes_data += write_low(self.transaction['type'])
        bytes_data += write_bit32(self.transaction['timestamp'])
        bytes_data += write_high(self.transaction['senderPublicKey'])
        bytes_data += write_bit64(self.transaction['fee'])

        if self.transaction.get('vendorField'):
            vendorFieldLength = len(self.transaction['vendorField'])
            bytes_data += write_bit8(vendorFieldLength)
            bytes_data += self.transaction['vendorField']
        elif self.transaction.get('vendorFieldHex'):
            vendorFieldHexLength = len(self.transaction['vendorFieldHex'])
            bytes_data += write_bit8(vendorFieldHexLength / 2)
            bytes_data += self.transaction['vendorFieldHex']
        else:
            bytes_data += write_bit8(0x00)

        bytes_data = self._handle_transaction_type(bytes_data)
        bytes_data = self._handle_signature(bytes_data)

        return bytes_data

    def _handle_transaction_type(self, bytes_data):
        """Serialize transaction specific data (eg. delegate registration)

        Args:
            bytes_data (bytes): already serialized data about a transaction (eg. version, network)

        Returns:
            bytes: bytes string
        """
        serializer_name = self.serializers[self.transaction['type']]

        module = import_module('crypto.serializers.{}'.format(serializer_name))
        for attr in dir(module):
            # If attr name is `BaseSerializer`, skip it as it's a class and also has a
            # subclass of BaseSerializer
            if attr == 'BaseSerializer':
                continue

            attribute = getattr(module, attr)
            if inspect.isclass(attribute) and issubclass(attribute, BaseSerializer):
                # this attribute is actually a specific serializer that we want to use
                serializer = attribute
                break
        return serializer(self.transaction, bytes_data).serialize()

    def _handle_signature(self, bytes_data):
        """Serialize signature data of the transaction

        Args:
            bytes_data (bytes): already serialized data

        Returns:
            bytes: bytes string
        """
        if self.transaction.get('signature'):
            bytes_data += unhexlify(self.transaction['signature'])

        if self.transaction.get('secondSignature'):
            bytes_data += unhexlify(self.transaction['secondSignature'])
        elif self.transaction.get('signSignature'):
            bytes_data += unhexlify(self.transaction['signSignature'])

        if self.transaction.get('signatures'):
            bytes_data += write_bit8(0xff)
            bytes_data += unhexlify(''.join(self.transaction['signatures']))

        return bytes_data
