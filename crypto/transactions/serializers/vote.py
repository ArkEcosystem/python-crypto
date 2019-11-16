from binascii import unhexlify

from binary.unsigned_integer.writer import write_bit8

from crypto.transactions.serializers.base import BaseSerializer


class VoteSerializer(BaseSerializer):
    """Serializer handling vote data
    """

    def serialize(self):
        vote_bytes = []

        for vote in self.transaction['asset']['votes']:
            if vote.startswith('+'):
                vote_bytes.append('01{}'.format(vote[1::]))
            else:
                vote_bytes.append('00{}'.format(vote[1::]))

        self.bytes_data += write_bit8(len(self.transaction['asset']['votes']))
        self.bytes_data += unhexlify(''.join(vote_bytes))

        return self.bytes_data
