from binascii import hexlify

from binary.unsigned_integer.reader import read_bit8

from crypto.transactions.deserializers.base import BaseDeserializer


class MultiSignatureRegistrationDeserializer(BaseDeserializer):

    def deserialize(self):
        starting_position = int(self.asset_offset / 2)

        self.transaction.asset = {
            'multiSignature': {
                'min': read_bit8(self.serialized, starting_position) & 0xff,
                'publicKeys': []
            }
        }

        count = read_bit8(self.serialized, starting_position + 1) & 0xff

        for index in range(count):
            index_start = int(self.asset_offset) + 4

            if (index > 0):
                index_start += index * 66
            public_key = hexlify(self.serialized)[index_start:index_start + 66].decode()
            self.transaction.asset['multiSignature']['publicKeys'].append(public_key)

        self.transaction.signatures = [] if self.transaction.signatures is None else self.transaction.signatures

        self.transaction.parse_signatures(
            hexlify(self.serialized).decode(),
            self.asset_offset + 4 + (count * 66)
        )

        return self.transaction
