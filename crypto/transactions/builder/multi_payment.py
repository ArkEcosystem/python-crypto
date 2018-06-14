from crypto.constants import TRANSACTION_MULTI_PAYMENT
from crypto.transactions.builder.base import BaseTransactionBuilder


class MultiPayment(BaseTransactionBuilder):

    transaction_type = TRANSACTION_MULTI_PAYMENT

    def __init__(self, fee=None):
        """Create a multi payment transaction

        Args:
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()
        if fee:
            self.transaction.fee = fee
