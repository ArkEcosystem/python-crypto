from binascii import unhexlify

from crypto.transactions.serializers.base import BaseSerializer


class HtlcRefundSerializer(BaseSerializer):
    """Serializer handling timelock refund data
    """

    def serialize(self):
        self.bytes_data += unhexlify(self.transaction['asset']['refund']['lockTransactionId'].encode())
        return self.bytes_data
