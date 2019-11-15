from binascii import hexlify, unhexlify

from binary.unsigned_integer.reader import read_bit8
from base58 import b58encode_check

from crypto.transactions.deserializers.base import BaseDeserializer


class IPFSDeserializer(BaseDeserializer):

    def deserialize(self):
        starting_position = int(self.asset_offset / 2)

        public_key = hexlify(self.serialized)[starting_position:starting_position + 66]

        ipfs_hash_length = read_bit8(self.serialized, starting_position) & 0xff
        start_index = self.asset_offset + 2
        end_index = start_index + (ipfs_hash_length * 2)
        ipfs_hash = hexlify(self.serialized)[start_index:end_index]
        print(ipfs_hash)
        ipfs_hash = b58encode_check(unhexlify(ipfs_hash)).decode() # Really not sure of that part
        print(ipfs_hash)

        self.transaction.asset = {
            'ipfs': ipfs_hash
        }

        self.transaction.parse_signatures(
            hexlify(self.serialized),
            self.asset_offset + (ipfs_hash_length + 2) * 2
        )

        print("SELF TRANSACTION")
        print(self.transaction.to_dict())

        return self.transaction
