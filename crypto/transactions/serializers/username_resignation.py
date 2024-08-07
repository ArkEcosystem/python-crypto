from crypto.transactions.serializers.base import BaseSerializer

class UsernameResignationSerializer(BaseSerializer):
    """Serializer handling username resignation data
    """

    def serialize(self) -> bytes:
        return self.bytes_data
