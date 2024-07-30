from binary.hex.writer import write_high

from crypto.transactions.serializers.base import BaseSerializer

class DelegateRegistrationSerializer(BaseSerializer):
    """Serializer handling delegate registration data
    """

    def serialize(self) -> bytes:
        delegate_bytes = self.transaction['asset']['validatorPublicKey'].encode()

        self.bytes_data += write_high(delegate_bytes)

        return self.bytes_data
