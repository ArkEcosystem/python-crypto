from crypto.constants import TRANSACTION_IPFS
from crypto.transactions.builder.base import BaseTransactionBuilder


class IPFS(BaseTransactionBuilder):

    transaction_type = TRANSACTION_IPFS

    def __init__(self, fee=None):
        """Create an ipfs transaction

        Args:
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()
        if fee:
            self.transaction.fee = fee
