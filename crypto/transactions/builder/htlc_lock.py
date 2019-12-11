from crypto.constants import TRANSACTION_HTLC_LOCK, TRANSACTION_TYPE_GROUP
from crypto.transactions.builder.base import BaseTransactionBuilder


class HtlcLock(BaseTransactionBuilder):

    transaction_type = TRANSACTION_HTLC_LOCK

    def __init__(self, recipient_id, secret_hash, expiration_type, expiration_value, fee=None):
        """Create a timelock transaction

        Args:
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        self.transaction.recipientId = recipient_id

        self.transaction.typeGroup = self.get_type_group()

        self.transaction.asset['lock'] = {
            'secretHash': secret_hash,
            'expiration': {
                'type': expiration_type,
                'value': expiration_value
            }
        }

        if fee:
            self.transaction.fee = fee

    def get_type_group(self):
        return TRANSACTION_TYPE_GROUP.CORE.value
