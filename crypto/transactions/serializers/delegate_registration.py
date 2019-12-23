from binascii import hexlify, unhexlify

from binary.unsigned_integer.writer import write_bit8

from crypto.transactions.serializers.base import BaseSerializer


class DelegateRegistrationSerializer(BaseSerializer):
    """Serializer handling delegate registration data
    """

    def serialize(self):
        delegate_bytes = hexlify(self.transaction['asset']['delegate']['username'].encode())

        self.bytes_data += write_bit8(len(delegate_bytes) // 2)
        self.bytes_data += unhexlify(delegate_bytes)

        return self.bytes_data
