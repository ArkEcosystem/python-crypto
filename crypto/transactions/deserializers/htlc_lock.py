from binascii import hexlify, unhexlify

from base58 import b58encode_check

from binary.unsigned_integer.reader import read_bit8, read_bit32, read_bit64

from crypto.transactions.deserializers.base import BaseDeserializer


class HtlcLockDeserializer(BaseDeserializer):

    def deserialize(self):
        starting_position = int(self.asset_offset / 2)

        self.transaction.amount = read_bit64(self.serialized, offset=starting_position)

        secret_hash = hexlify(self.serialized)[(starting_position + 8) * 2:(starting_position + 8 + 32) * 2]

        expiration_type = read_bit8(self.serialized, offset=99)

        expiration_value = read_bit32(self.serialized, offset=100)

        recipient_start_index = (starting_position + 45) * 2
        recipientId = hexlify(self.serialized)[recipient_start_index:recipient_start_index + 42]
        self.transaction.recipientId = b58encode_check(unhexlify(recipientId)).decode()

        self.transaction.asset['lock'] = {
            'secretHash': secret_hash.decode()
        }

        self.transaction.asset['lock']['expiration'] = {
            'type': expiration_type,
            'value': expiration_value
        }

        self.transaction.parse_signatures(
            hexlify(self.serialized).decode(),
            self.asset_offset + (8 + 32 + 1 + 4 + 21) * 2
        )

        return self.transaction
