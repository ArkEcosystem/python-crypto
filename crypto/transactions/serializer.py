import inspect
from binascii import hexlify, unhexlify
from importlib import import_module

from binary.hex.writer import write_high
from binary.unsigned_integer.writer import write_bit8, write_bit16, write_bit32, write_bit64

from crypto.configuration.network import get_network
from crypto.constants import TRANSACTION_TYPES
from crypto.exceptions import ArkSerializerException
from crypto.transactions.serializers.base import BaseSerializer


class Serializer(object):

    transaction = None

    def __init__(self, transaction):
        if not transaction:
            raise ArkSerializerException('No transaction data provided')
        self.transaction = transaction

    def serialize(self, skip_signature=True, skip_second_signature=True, skip_multi_signature=True, raw=False):
        """Perform AIP11 compliant serialization

        Returns:
            bytes: bytes string
        """
        network_config = get_network()
        bytes_data = bytes()

        bytes_data += write_bit8(0xff)

        bytes_data += write_bit8(self.transaction.get('version') or 0x02)
        bytes_data += write_bit8(self.transaction.get('network') or network_config['version'])
        bytes_data += write_bit32(self.transaction.get('typeGroup') or 0x01)
        bytes_data += write_bit16(self.transaction.get('type'))
        bytes_data += write_bit64(self.transaction.get('nonce') or 0x01)

        bytes_data += write_high(self.transaction.get('senderPublicKey'))
        bytes_data += write_bit64(self.transaction.get('fee'))

        if self.transaction.get('vendorField'):
            vendorFieldLength = len(self.transaction.get('vendorField'))
            bytes_data += write_bit8(vendorFieldLength)
            bytes_data += self.transaction['vendorField'].encode()
        elif self.transaction.get('vendorFieldHex'):
            vendorField_hex_length = len(self.transaction['vendorFieldHex'])
            bytes_data += write_bit8(vendorField_hex_length / 2)
            bytes_data += self.transaction['vendorFieldHex']
        else:
            bytes_data += write_bit8(0x00)
        bytes_data = self._handle_transaction_type(bytes_data)
        bytes_data = self._handle_signature(bytes_data, skip_signature, skip_second_signature, skip_multi_signature)

        return bytes_data if raw else hexlify(bytes_data).decode()

    def _handle_transaction_type(self, bytes_data):
        """Serialize transaction specific data (eg. delegate registration)

        Args:
            bytes_data (bytes): already serialized data about a transaction (eg. version, network)

        Returns:
            bytes: bytes string
        """
        serializer_name = TRANSACTION_TYPES[self.transaction['type']]

        module = import_module('crypto.transactions.serializers.{}'.format(serializer_name))
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

    def _handle_signature(self, bytes_data, skip_signature, skip_second_signature, skip_multi_signature):
        """Serialize signature data of the transaction

        Args:
            bytes_data (bytes): already serialized data

        Returns:
            bytes: bytes string
        """
        if not skip_signature and self.transaction.get('signature'):
            bytes_data += unhexlify(self.transaction['signature'])

        if not skip_second_signature and self.transaction.get('secondSignature'):
            bytes_data += unhexlify(self.transaction['secondSignature'])
        if not skip_second_signature and self.transaction.get('signSignature'):
            bytes_data += unhexlify(self.transaction['signSignature'])
        if not skip_multi_signature and self.transaction.get('signatures'):
            bytes_data += unhexlify(''.join(self.transaction['signatures']))

        return bytes_data
