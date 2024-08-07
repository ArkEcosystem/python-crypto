from binascii import hexlify

from crypto.transactions.deserializers.base import BaseDeserializer

class UsernameResignationDeserializer(BaseDeserializer):
    def deserialize(self):
        self.transaction.parse_signatures(
            hexlify(self.serialized).decode(),
            self.asset_offset
        )

        return self.transaction
