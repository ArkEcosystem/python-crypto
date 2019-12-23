from binascii import hexlify, unhexlify

from base58 import b58encode_check

from binary.unsigned_integer.reader import read_bit32, read_bit64

from crypto.transactions.deserializers.base import BaseDeserializer


class TransferDeserializer(BaseDeserializer):

    def deserialize(self):
        starting_position = int(self.asset_offset / 2)

        self.transaction.amount = read_bit64(self.serialized, offset=starting_position)
        self.transaction.expiration = read_bit32(self.serialized, offset=starting_position + 8)

        recipient_start_index = (int(self.asset_offset / 2) + 12) * 2
        recipientId = hexlify(self.serialized)[recipient_start_index:recipient_start_index + 42]
        self.transaction.recipientId = b58encode_check(unhexlify(recipientId)).decode()

        self.transaction.parse_signatures(
            hexlify(self.serialized).decode(),
            self.asset_offset + (8 + 4 + 21) * 2
        )

        return self.transaction
