from crypto.constants import TRANSACTION_FEES, TRANSACTION_IPFS
from crypto.transactions.builder.base import BaseTransactionBuilder


class IPFSTransaction(BaseTransactionBuilder):

    transaction_type = TRANSACTION_IPFS

    def __init__(self, fee=None):
        """Create an ipfs transaction

        Args:
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()
        self.transaction.fee = fee or TRANSACTION_FEES[self.transaction_type]

    def handle_transaction_type(self, bytes_data):
        raise NotImplementedError
