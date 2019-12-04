from binascii import hexlify, unhexlify

from binary.unsigned_integer.reader import read_bit8

from crypto.transactions.deserializers.base import BaseDeserializer


class HtlcRefundDeserializer(BaseDeserializer):

    def deserialize(self):
        starting_position = int(self.asset_offset)

        lock_transaction_id = hexlify(self.serialized)[starting_position:starting_position + 64]

        self.transaction.asset['refund'] = {
            'lockTransactionId': lock_transaction_id.decode()
        }

        self.transaction.parse_signatures(
            hexlify(self.serialized).decode(),
            self.asset_offset + 64
        )

        return self.transaction
