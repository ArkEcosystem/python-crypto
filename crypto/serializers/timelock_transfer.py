from base58 import b58decode_check

from binascii import hexlify

from binary.hex.writer import write_high, write_low
from binary.unsigned_integer.writer import write_bit32, write_bit64

from crypto.serializers.base import BaseSerializer


class TimelockTransferSerializer(BaseSerializer):
    """Serializer handling timelock transfer data
    """

    def serialize(self):
        self.bytes_data += write_bit64(self.transaction['recipientId']['amount'])
        self.bytes_data += write_low(self.transaction['recipientId']['timelocktype'])
        self.bytes_data += write_bit32(self.transaction['recipientId']['timelock'])
        recipient_id = hexlify(b58decode_check(self.transaction['recipientId']))
        self.bytes_data += write_high(recipient_id)
        return self.bytes_data
