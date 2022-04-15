from crypto.constants import TRANSACTION_HTLC_CLAIM, TRANSACTION_TYPE_GROUP
from crypto.exceptions import ArkInvalidTransaction
from crypto.transactions.builder.base import BaseTransactionBuilder


class HtlcClaim(BaseTransactionBuilder):

    transaction_type = TRANSACTION_HTLC_CLAIM

    def __init__(self, lock_transaction_id, unlock_secret, fee=None):
        """Create a timelock transaction

        Args:
            lock_transaction_id (str): HTLC lock transaction ID we wish to claim
            unlock_secret (str): unlock secret required to claim the transaction, must be 64 chars long
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        self.transaction.typeGroup = self.get_type_group()

        self.transaction.asset['claim'] = {
            'lockTransactionId': lock_transaction_id,
            'unlockSecret': unlock_secret
        }

        if fee:
            self.transaction.fee = fee

    def get_type_group(self):
        return TRANSACTION_TYPE_GROUP.CORE.value
