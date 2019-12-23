from crypto.constants import TRANSACTION_IPFS, TRANSACTION_TYPE_GROUP
from crypto.transactions.builder.base import BaseTransactionBuilder


class IPFS(BaseTransactionBuilder):

    transaction_type = TRANSACTION_IPFS

    def __init__(self, ipfs_id, fee=None):
        """Create an ipfs transaction

        Args:
            ipfs_id (str): ipfs transaction identifier
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        self.transaction.asset['ipfs'] = ipfs_id
        self.transaction.typeGroup = self.get_type_group()

        if fee:
            self.transaction.fee = fee

    def get_type_group(self):
        return TRANSACTION_TYPE_GROUP.CORE.value
