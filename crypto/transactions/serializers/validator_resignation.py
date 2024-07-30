from crypto.transactions.serializers.base import BaseSerializer

class ValidatorResignationSerializer(BaseSerializer):
    """Serializer handling validator resignation data
    """

    def serialize(self) -> bytes:
        return self.bytes_data
