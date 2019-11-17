from binascii import hexlify

from crypto.transactions.deserializers.base import BaseDeserializer

class HtlcClaimDeserializer(BaseDeserializer):

    def deserialize(self):
        starting_position = int(self.asset_offset)

        lock_transaction_id = hexlify(self.serialized)[starting_position:starting_position + (32 * 2)]
        unlock_secret = hexlify(self.serialized)[starting_position:starting_position + 64 * 2]

        self.transaction.asset['claim'] = {
            'lockTransactionId': lock_transaction_id.decode(),
            'unlockSecret': unlock_secret.decode()
        }

        self.transaction.parse_signatures(
            hexlify(self.serialized),
            self.asset_offset + 64 + 64
        )

        return self.transaction
