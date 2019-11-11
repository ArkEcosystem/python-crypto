from crypto.constants import TRANSACTION_TIMELOCK_REFUND
from crypto.transactions.builder.base import BaseTransactionBuilder


class TimelockRefund(BaseTransactionBuilder):

    transaction_type = TRANSACTION_TIMELOCK_REFUND

    def __init__(self, fee=None):
        """Create a timelock transaction

        Args:
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()
        if fee:
            self.transaction.fee = fee
