from binary.hex.writer import write_high

from crypto.transactions.serializers.base import BaseSerializer

class ValidatorRegistrationSerializer(BaseSerializer):
    """Serializer handling validator registration data
    """

    def serialize(self) -> bytes:
        validator_bytes = self.transaction['asset']['validatorPublicKey'].encode()

        self.bytes_data += write_high(validator_bytes)

        return self.bytes_data
