from binary.hex.writer import write_high
from binary.unsigned_integer.writer import write_bit16, write_bit64

from crypto.transactions.serializers.base import BaseSerializer


class MultiPaymentSerializer(BaseSerializer):
    """Serializer handling multi payment data
    """

    def serialize(self):
        self.bytes_data += write_bit16(len(self.transaction['asset']['payments']))

        for payment in self.transaction['asset']['payments']:
            recipient = payment['recipientId'][2:]

            if type(recipient) is str:
                recipient = recipient.encode()

            self.bytes_data += write_bit64(payment['amount'])
            self.bytes_data += write_high(recipient)

        return self.bytes_data
