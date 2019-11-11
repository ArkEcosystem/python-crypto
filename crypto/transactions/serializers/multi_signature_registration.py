from binascii import unhexlify

from binary.unsigned_integer.writer import write_bit8

from crypto.transactions.serializers.base import BaseSerializer


class DelegateRegistrationSerializer(BaseSerializer):
    """Serializer handling delegate registration data
    """

    def serialize(self):
        publicKeys = []
        if self.transaction.get('version') is None or self.transaction['version'] == 1:
            for key in self.transaction['asset']['multiSignature']['publicKeys']:
                publicKeys.append(key[1::] if key.startswith('+') else key)
        else:
            publicKeys = self.transaction['asset']['multiSignature']['publicKeys']
        self.bytes_data += write_bit8(self.transaction['asset']['multiSignature']['min'])
        self.bytes_data += write_bit8(len(self.transaction['asset']['multiSignature']['publicKeys']))
        self.bytes_data += write_bit8(self.transaction['asset']['multiSignature']['lifetime'])
        self.bytes_data += unhexlify(''.join(publicKeys))
        return self.bytes_data
