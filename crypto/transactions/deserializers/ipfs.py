from binascii import hexlify, unhexlify

from base58 import b58encode

from binary.unsigned_integer.reader import read_bit8
from binary.unsigned_integer.writer import write_bit8

from crypto.transactions.deserializers.base import BaseDeserializer


class IPFSDeserializer(BaseDeserializer):

    def deserialize(self):
        starting_position = int(self.asset_offset / 2)

        hash_function = read_bit8(self.serialized, starting_position) & 0xff
        ipfs_hash_length = read_bit8(self.serialized, starting_position + 1) & 0xff

        start_index = (starting_position + 2) * 2
        end_index = start_index + (ipfs_hash_length * 2)
        ipfs_hash = hexlify(self.serialized)[start_index:end_index]

        temp_buffer = bytes()

        temp_buffer += write_bit8(hash_function)
        temp_buffer += write_bit8(ipfs_hash_length)
        temp_buffer += unhexlify(ipfs_hash)

        self.transaction.asset = {
            'ipfs': b58encode(temp_buffer).decode()
        }

        self.transaction.parse_signatures(
            hexlify(self.serialized).decode(),
            self.asset_offset + (ipfs_hash_length + 2) * 2
        )

        return self.transaction
