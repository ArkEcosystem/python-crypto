from base58 import b58decode_check

from binascii import hexlify

from binary.hex.writer import write_high
from binary.unsigned_integer.writer import write_bit32, write_bit64

from crypto.serializers.base import BaseSerializer


class MultiPaymentSerializer(BaseSerializer):
    """Serializer handling multi payment data
    """

    def serialize(self):
        self.bytes_data += write_bit32(len(self.transaction['asset']['payments']))
        for payment in self.transaction['asset']['payments']:
            self.bytes_data += write_bit64(payment['amount'])
            recipient_id = b58decode_check(hexlify(payment['recipientId']).encode())
            self.bytes_data += write_high(recipient_id)
        return self.bytes_data
