from binascii import hexlify, unhexlify

from crypto.transactions.serializers.base import BaseSerializer
from crypto.exceptions import ArkSerializerException


class HtlcClaimSerializer(BaseSerializer):
    """Serializer handling timelock claim data
    """

    def serialize(self):
        self.bytes_data += unhexlify(self.transaction['asset']['claim']['lockTransactionId'])
        unlock_secret_bytes = unhexlify(self.transaction['asset']['claim']['unlockSecret'].encode())
        if len(unlock_secret_bytes) != 32:
            raise ArkSerializerException("Unlock secret must be 32 bytes long")
        self.bytes_data += unhexlify(self.transaction['asset']['claim']['unlockSecret'].encode())


        return self.bytes_data
