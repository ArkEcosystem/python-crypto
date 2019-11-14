from binascii import hexlify, unhexlify

from binary.unsigned_integer.writer import write_bit8
from base58 import b58decode_check, b58encode_check, b58encode, b58decode

from binary.hex.writer import write_high
from crypto.transactions.serializers.base import BaseSerializer


class IPFSSerializer(BaseSerializer):
    """Serializer handling ipfs data
    """

    def serialize(self):
        dag = hexlify(b58decode(self.transaction['asset']['ipfs']))
        self.bytes_data += write_high(dag)
        return self.bytes_data
