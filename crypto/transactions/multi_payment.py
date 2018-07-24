from crypto.constants import TRANSACTION_FEES, TRANSACTION_MULTI_PAYMENT
from crypto.transactions.base import Transaction


class IPFSTransaction(Transaction):

    transaction_type = TRANSACTION_MULTI_PAYMENT

    def __init__(self, fee=None):
        """Create a multi payment transaction

        Args:
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()
        self.fee = fee or TRANSACTION_FEES[self.transaction_type]

    def handle_transaction_type(self, bytes_data):
        raise NotImplementedError
