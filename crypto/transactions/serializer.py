from binascii import unhexlify
from crypto.transactions.types.abstract_transaction import AbstractTransaction
from crypto.configuration.network import get_network
from binary.unsigned_integer.writer import (
    write_bit8,
    write_bit32,
    write_bit64,
)
# from crypto.utils.address import Address  # TODO: Implement or import Address


class Serializer:
    def __init__(self, transaction: AbstractTransaction):
        if not transaction:
            raise ValueError('No transaction data provided')
        self.transaction = transaction

    @staticmethod
    def new(transaction: AbstractTransaction):
        return Serializer(transaction)

    @staticmethod
    def get_bytes(transaction: AbstractTransaction, skip_signature: bool = False) -> bytes:
        return transaction.serialize(skip_signature=skip_signature)

    def serialize(self, skip_signature: bool = False) -> bytes:
        bytes_data = bytes()

        bytes_data += self.serialize_common()
        bytes_data += self.serialize_data()
        if not skip_signature:
            bytes_data += self.serialize_signatures()

        return bytes_data

    def serialize_common(self) -> bytes:
        bytes_data = bytes()
        network_version = self.transaction.data.get('network', get_network()['version'])
        bytes_data += write_bit8(int(network_version))
        bytes_data += write_bit64(int(self.transaction.data['nonce']))
        bytes_data += write_bit32(int(self.transaction.data['gasPrice']))
        bytes_data += write_bit32(int(self.transaction.data['gasLimit']))
        return bytes_data

    def serialize_data(self) -> bytes:
        bytes_data = bytes()
        
        bytes_data += int(self.transaction.data['value']).to_bytes(32, byteorder='big')

        if 'recipientAddress' in self.transaction.data:
            bytes_data += write_bit8(1)
            recipient_address = self.transaction.data['recipientAddress']
            bytes_data += unhexlify(recipient_address.replace('0x', ''))
        else:
            bytes_data += write_bit8(0)

        payload_hex = self.transaction.data.get('data', '')
        payload_length = len(payload_hex) // 2
        bytes_data += write_bit32(payload_length)

        if payload_length > 0:
            bytes_data += unhexlify(payload_hex)

        return bytes_data

    def serialize_signatures(self) -> bytes:
        bytes_data = bytes()
        if 'signature' in self.transaction.data:
            bytes_data += unhexlify(self.transaction.data['signature'])
        return bytes_data
