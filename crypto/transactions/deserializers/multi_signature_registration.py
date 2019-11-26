from binascii import hexlify

from binary.unsigned_integer.reader import read_bit8

from crypto.transactions.deserializers.base import BaseDeserializer


class MultiSignatureRegistrationDeserializer(BaseDeserializer):

    def deserialize(self):
        starting_position = int(self.asset_offset / 2)

        if self.transaction.version is None or self.transaction.version == 1:
            self.transaction.asset = {
                'multiSignatureLegacy': {
                    'min': read_bit8(self.serialized, starting_position) & 0xff,
                    'lifetime': read_bit8(self.serialized, starting_position + 2) & 0xff,
                    'keysgroup': []
                }
            }

            keys_group_count = read_bit8(self.serialized, starting_position + 1) & 0xff

            for index in range(keys_group_count):
                index_start = int(self.asset_offset) + 4

                if (index > 0):
                    index_start += index * 66
                signature = hexlify(self.serialized)[index_start:index_start + 66].decode()
                self.transaction.asset['multiSignatureLegacy']['keysgroup'].append(signature)
        else:
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
                signature = hexlify(self.serialized)[index_start:index_start + 66].decode()
                self.transaction.asset['multiSignature']['publicKeys'].append(signature)

        self.transaction.parse_signatures(
            hexlify(self.serialized),
            self.asset_offset + 6 + (count * 66)
        )

        return self.transaction
