from binascii import hexlify

from base58 import b58decode_check

from binary.hex.writer import write_high, write_low
from binary.unsigned_integer.writer import write_bit32, write_bit64

from crypto.transactions.serializers.base import BaseSerializer


class TimelockTransferSerializer(BaseSerializer):
    """Serializer handling timelock transfer data
    """

    def serialize(self):
        self.bytes_data += write_bit64(self.transaction['recipientId']['amount'])
        self.bytes_data += write_low(self.transaction['recipientId']['timelocktype'])
        self.bytes_data += write_bit32(self.transaction['recipientId']['timelock'])
        recipientId = hexlify(b58decode_check(self.transaction['recipientId']))
        self.bytes_data += write_high(recipientId)
        return self.bytes_data
