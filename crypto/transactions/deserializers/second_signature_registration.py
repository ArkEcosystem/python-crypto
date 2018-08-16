from binascii import hexlify

from crypto.transactions.deserializers.base import BaseDeserializer


class SecondSignatureRegistrationDeserializer(BaseDeserializer):

    def deserialize(self):
        starting_position = int(self.asset_offset)

        self.transaction.asset = {
            'signature': {
                'publicKey': hexlify(self.serialized)[starting_position:starting_position + 66].decode()
            }
        }

        self.transaction.parse_signatures(hexlify(self.serialized), self.asset_offset + 66)
        return self.transaction
