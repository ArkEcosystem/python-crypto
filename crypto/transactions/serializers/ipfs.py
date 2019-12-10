from binascii import hexlify

from base58 import b58decode

from binary.hex.writer import write_high

from crypto.transactions.serializers.base import BaseSerializer


class IPFSSerializer(BaseSerializer):
    """Serializer handling ipfs data
    """

    def serialize(self):
        ipfs = hexlify(b58decode(self.transaction['asset']['ipfs']))

        self.bytes_data += write_high(ipfs)

        return self.bytes_data
