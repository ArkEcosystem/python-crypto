from binascii import unhexlify

from binary.unsigned_integer.writer import write_bit8

from crypto.transactions.serializers.base import BaseSerializer


class IPFSSerializer(BaseSerializer):
    """Serializer handling ipfs data
    """

    def serialize(self):
        dag = self.transaction['asset']['ipfs']['dag']
        self.bytes_data += write_bit8(len(dag) // 2)
        self.bytes_data += unhexlify(dag)
        return self.bytes_data
