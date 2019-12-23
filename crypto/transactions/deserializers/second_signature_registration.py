from binascii import hexlify

from crypto.transactions.deserializers.base import BaseDeserializer


class SecondSignatureRegistrationDeserializer(BaseDeserializer):

    def deserialize(self):
        starting_position = int(self.asset_offset)

        public_key = hexlify(self.serialized)[starting_position:starting_position + 66]

        self.transaction.asset = {
            'signature': {
                'publicKey': public_key.decode()
            }
        }

        self.transaction.parse_signatures(hexlify(self.serialized).decode(), self.asset_offset + 66)

        return self.transaction
