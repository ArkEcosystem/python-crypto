from binascii import hexlify

from binary.unsigned_integer.reader import read_bit8

from crypto.transactions.deserializers.base import BaseDeserializer


class VoteDeserializer(BaseDeserializer):

    def deserialize(self):
        starting_position = int(self.asset_offset / 2)

        vote_length = read_bit8(self.serialized, starting_position) & 0xff

        self.transaction.asset['votes'] = []

        for index in range(vote_length):
            starting_position = self.asset_offset + 2 + (index * 2 * 34)
            vote = hexlify(self.serialized)[starting_position:starting_position + 2 * 34].decode()
            if vote[1] == '1':
                operator = '+'
            else:
                operator = '-'
            vote = '{}{}'.format(operator, vote[2:])

            self.transaction.asset['votes'].append(vote)

        self.transaction.parse_signatures(
            hexlify(self.serialized).decode(),
            self.asset_offset + 2 + (vote_length * 34 * 2)
        )

        return self.transaction
