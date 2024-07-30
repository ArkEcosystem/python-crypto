from binascii import hexlify
from binary.unsigned_integer.reader import read_bit8

from crypto.transactions.deserializers.base import BaseDeserializer

class VoteDeserializer(BaseDeserializer):
    def deserialize(self):
        starting_position = int(self.asset_offset / 2)

        vote_length = read_bit8(self.serialized, starting_position) & 0xff

        self.transaction.asset['votes'] = []
        self.transaction.asset['unvotes'] = []

        vote_position = starting_position + 1

        for index in range(vote_length):
            vote = self.serialized[vote_position + (index * 33):vote_position + (index * 33) + 33].hex()

            self.transaction.asset['votes'].append(vote)

        unvote_position = vote_position + (vote_length * 33)

        unvote_length = read_bit8(self.serialized, unvote_position) & 0xff

        unvote_position += 1

        for index in range(unvote_length):
            unvote = self.serialized[unvote_position + (index * 33):unvote_position + (index * 33) + 33].hex()

            self.transaction.asset['unvotes'].append(unvote)

        self.transaction.parse_signatures(
            hexlify(self.serialized).decode(),
            self.asset_offset + 2 + (vote_length * 66) + 2 + (unvote_length * 66)
        )

        return self.transaction
