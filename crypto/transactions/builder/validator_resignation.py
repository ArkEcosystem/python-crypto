from typing import Optional

from crypto.constants import TRANSACTION_VALIDATOR_RESIGNATION, TRANSACTION_TYPE_GROUP
from crypto.transactions.builder.base import BaseTransactionBuilder

class ValidatorResignation(BaseTransactionBuilder):
    transaction_type = TRANSACTION_VALIDATOR_RESIGNATION

    def __init__(self, fee: Optional[int] = None):
        """Create a validator resignation transaction

        Args:
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        self.transaction.typeGroup = self.get_type_group()

        if fee:
            self.transaction.fee = fee

    def get_type_group(self) -> int:
        return TRANSACTION_TYPE_GROUP.CORE.value
