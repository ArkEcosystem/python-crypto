from binascii import unhexlify

from binary.unsigned_integer.writer import write_bit8

from crypto.transactions.serializers.base import BaseSerializer


class MultiSignatureSerializer(BaseSerializer):
    """Serializer handling delegate registration data
    """

    def serialize(self):
        public_keys_length = len(self.transaction['asset']['multiSignature']['publicKeys'])
        self.bytes_data += write_bit8(self.transaction['asset']['multiSignature']['min'])
        self.bytes_data += write_bit8(public_keys_length)
        for key in self.transaction['asset']['multiSignature']['publicKeys']:
            self.bytes_data += unhexlify(key.encode())

        return self.bytes_data
