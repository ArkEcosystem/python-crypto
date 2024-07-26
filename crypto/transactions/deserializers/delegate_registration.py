from binascii import hexlify

from crypto.transactions.deserializers.base import BaseDeserializer


class DelegateRegistrationDeserializer(BaseDeserializer):

    def deserialize(self):
        starting_position = int(self.asset_offset / 2)

        validator_public_key = self.serialized[starting_position:starting_position + 48]

        self.transaction.asset['validatorPublicKey'] = validator_public_key.hex()

        self.transaction.parse_signatures(
            hexlify(self.serialized).decode(),
            self.asset_offset + (48 * 2)
        )

        return self.transaction
