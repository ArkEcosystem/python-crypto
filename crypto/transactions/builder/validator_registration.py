from typing import Optional

from crypto.constants import TRANSACTION_VALIDATOR_REGISTRATION
from crypto.transactions.builder.base import BaseTransactionBuilder

class ValidatorRegistration(BaseTransactionBuilder):
    transaction_type = TRANSACTION_VALIDATOR_REGISTRATION

    def __init__(self, public_key: str, fee: Optional[int] = None):
        """Create a validator registration transaction

        Args:
            public_key (str): BLS public key of a validator you want to register
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        self.transaction.asset['validatorPublicKey'] = public_key

        if fee:
            self.transaction.fee = fee
