from crypto.constants import TRANSACTION_DELEGATE_RESIGNATION, TRANSACTION_FEES
from crypto.transactions.builder.base import BaseTransactionBuilder


class DelegateResignationTransaction(BaseTransactionBuilder):

    transaction_type = TRANSACTION_DELEGATE_RESIGNATION

    def __init__(self, fee=None):
        """Create a delegate resignation transaction

        Args:
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()
        self.transaction.fee = fee or TRANSACTION_FEES[self.transaction_type]

    def handle_transaction_type(self, bytes_data):
        raise NotImplementedError