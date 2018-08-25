from crypto.constants import TRANSACTION_DELEGATE_RESIGNATION
from crypto.transactions.builder.base import BaseTransactionBuilder


class DelegateResignation(BaseTransactionBuilder):

    transaction_type = TRANSACTION_DELEGATE_RESIGNATION

    def __init__(self, fee=None):
        """Create a delegate resignation transaction

        Args:
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()
        if fee:
            self.transaction.fee = fee
