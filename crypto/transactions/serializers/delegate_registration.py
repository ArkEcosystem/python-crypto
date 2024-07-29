from binascii import hexlify, unhexlify

from binary.unsigned_integer.writer import write_bit8

from crypto.transactions.serializers.base import BaseSerializer
from binary.hex.writer import write_high

class DelegateRegistrationSerializer(BaseSerializer):
    """Serializer handling delegate registration data
    """

    def serialize(self):
        delegate_bytes = self.transaction['asset']['validatorPublicKey'].encode()

        self.bytes_data += write_high(delegate_bytes)

        return self.bytes_data
