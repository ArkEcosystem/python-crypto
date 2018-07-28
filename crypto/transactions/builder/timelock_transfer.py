from crypto.constants import TRANSACTION_FEES, TRANSACTION_TIMELOCK_TRANSFER
from crypto.transactions.builder.base import BaseTransactionBuilder


class TimelockTransferTransaction(BaseTransactionBuilder):

    transaction_type = TRANSACTION_TIMELOCK_TRANSFER

    def __init__(self, fee=None):
        """Create a timelock transaction

        Args:
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()
        self.transaction.fee = fee or TRANSACTION_FEES[self.transaction_type]

    def handle_transaction_type(self, bytes_data):
        raise NotImplementedError