from binascii import hexlify, unhexlify

from binary.unsigned_integer.reader import read_bit16, read_bit64

from crypto.identity.address import get_checksum_address
from crypto.transactions.deserializers.base import BaseDeserializer


class MultiPaymentDeserializer(BaseDeserializer):

    def deserialize(self):
        starting_position = int(self.asset_offset / 2)

        payment_length = read_bit16(self.serialized, starting_position) & 0xff

        self.transaction.asset['payments'] = []

        index = 0

        for _ in range(payment_length):
            amount = read_bit64(self.serialized, offset=starting_position + 2 + index)

            recipient_start_index = (starting_position + 10 + index) * 2
            recipientId = hexlify(self.serialized)[recipient_start_index:recipient_start_index + 40]

            self.transaction.asset['payments'].append({'amount': amount, 'recipientId': get_checksum_address('0x'+ unhexlify(recipientId).hex())})

            index += 20 + 8

        self.transaction.parse_signatures(
            hexlify(self.serialized).decode(),
            self.asset_offset + 4 + (payment_length * (20 + 8)) * 2
        )

        return self.transaction
