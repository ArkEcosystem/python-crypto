from binascii import unhexlify

from binary.unsigned_integer.writer import write_bit8

from crypto.transactions.serializers.base import BaseSerializer


class DelegateRegistrationSerializer(BaseSerializer):
    """Serializer handling delegate registration data
    """

    def serialize(self):
        keysgroup = []
        if self.transaction.get('version') is None or self.transaction['version'] == 1:
            for key in self.transaction['asset']['multisignature']['keysgroup']:
                keysgroup.append(key[1::] if key.startswith('+') else key)
        else:
            keysgroup = self.transaction['asset']['multisignature']['keysgroup']
        self.bytes_data += write_bit8(self.transaction['asset']['multisignature']['min'])
        self.bytes_data += write_bit8(len(self.transaction['asset']['multisignature']['keysgroup']))
        self.bytes_data += write_bit8(self.transaction['asset']['multisignature']['lifetime'])
        self.bytes_data += unhexlify(''.join(keysgroup))
        return self.bytes_data
