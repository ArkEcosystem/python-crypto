from binascii import unhexlify

from crypto.transactions.serializers.base import BaseSerializer


class SecondSignatureRegistrationSerializer(BaseSerializer):
    """Serializer handling registration of the seconds signature
    """

    def serialize(self):
        self.bytes_data += unhexlify(self.transaction['asset']['signature']['publicKey'].encode())
        return self.bytes_data
