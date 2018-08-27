from crypto.transactions.serializers.base import BaseSerializer


class DelegateResignationSerializer(BaseSerializer):
    """Serializer handling delegate resignation data
    """

    def serialize(self):
        return self.bytes_data
