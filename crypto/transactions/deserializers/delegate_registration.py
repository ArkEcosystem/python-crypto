from binascii import hexlify, unhexlify

from binary.unsigned_integer.reader import read_bit8

from crypto.transactions.deserializers.base import BaseDeserializer


class DelegateRegistrationDeserializer(BaseDeserializer):

    def deserialize(self):
        starting_position = int(self.asset_offset / 2)

        username_length = read_bit8(self.serialized, starting_position) & 0xff
        start_index = self.asset_offset + 2
        end_index = start_index + (username_length * 2)
        username = hexlify(self.serialized)[start_index:end_index]
        username = unhexlify(username)

        self.transaction.asset['delegate'] = {'username': username.decode()}

        self.transaction.parse_signatures(
            hexlify(self.serialized).decode(),
            self.asset_offset + (username_length + 1) * 2
        )

        return self.transaction
