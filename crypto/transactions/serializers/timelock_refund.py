from binascii import unhexlify

from crypto.transactions.serializers.base import BaseSerializer


class TimelockRefundSerializer(BaseSerializer):
    """Serializer handling timelock claim data
    """

    def serialize(self):
        self.bytes_data += unhexlify(self.transaction['asset']['refund']['lockTransactionId'].encode())
        return self.bytes_data
