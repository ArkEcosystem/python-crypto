from binascii import hexlify, unhexlify
from binary.hex.writer import write_high
from binary.unsigned_integer.writer import write_bit8

from crypto.transactions.serializers.base import BaseSerializer

class UsernameRegistrationSerializer(BaseSerializer):
    """Serializer handling username registration data
    """

    def serialize(self) -> bytes:
        username_bytes = hexlify(self.transaction['asset']['username'].encode())

        self.bytes_data += write_bit8(len(username_bytes) // 2)
        self.bytes_data += unhexlify(username_bytes)

        return self.bytes_data
