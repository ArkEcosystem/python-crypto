from binascii import unhexlify
from binary.unsigned_integer.writer import write_bit8

from crypto.transactions.serializers.base import BaseSerializer

class VoteSerializer(BaseSerializer):
    """Serializer handling vote data
    """

    def serialize(self) -> bytes:
        vote_bytes = []
        unvote_bytes = []

        for vote in self.transaction['asset']['votes']:
            vote_bytes.append(vote)

        for unvote in self.transaction['asset']['unvotes']:
            unvote_bytes.append(unvote)

        self.bytes_data += write_bit8(len(self.transaction['asset']['votes']))
        self.bytes_data += unhexlify(''.join(vote_bytes))

        self.bytes_data += write_bit8(len(self.transaction['asset']['unvotes']))
        self.bytes_data += unhexlify(''.join(unvote_bytes))

        return self.bytes_data
