from binascii import unhexlify, hexlify

from binary.unsigned_integer.writer import write_bit8

from crypto.transactions.serializers.base import BaseSerializer


class MultiSignatureSerializer(BaseSerializer):
    """Serializer handling delegate registration data
    """

    def serialize(self):
        publicKeys = []

        if self.transaction.get('version') is None or self.transaction['version'] == 1:
            for key in self.transaction['asset']['multiSignatureLegacy']['keysgroup']:
                publicKeys.append(key[1::] if key.startswith('+') else key)
            self.bytes_data += write_bit8(self.transaction['asset']['multiSignatureLegacy']['min'])
            self.bytes_data += write_bit8(len(self.transaction['asset']['multiSignatureLegacy']['keysgroup']))
            self.bytes_data += write_bit8(self.transaction['asset']['multiSignatureLegacy']['lifetime'])
            self.bytes_data += unhexlify(''.join(publicKeys))
        else:
            public_keys_length = len(self.transaction['asset']['multiSignature']['publicKeys'])
            self.bytes_data += write_bit8(self.transaction['asset']['multiSignature']['min'])
            self.bytes_data += write_bit8(public_keys_length)
            for key in self.transaction['asset']['multiSignature']['publicKeys']:
                self.bytes_data += unhexlify(key.encode())
        return self.bytes_data
