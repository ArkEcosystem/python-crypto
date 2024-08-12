from typing import Optional

from crypto.constants import TRANSACTION_USERNAME_REGISTRATION
from crypto.transactions.builder.base import BaseTransactionBuilder

class UsernameRegistration(BaseTransactionBuilder):
    transaction_type = TRANSACTION_USERNAME_REGISTRATION

    def __init__(self, username: str, fee: Optional[int] = None):
        """Create a username registration transaction

        Args:
            username (str): username you want to register
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        self.transaction.asset['username'] = username

        if fee:
            self.transaction.fee = fee
