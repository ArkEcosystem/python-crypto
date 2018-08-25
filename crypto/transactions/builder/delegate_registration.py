from crypto.constants import TRANSACTION_DELEGATE_REGISTRATION
from crypto.transactions.builder.base import BaseTransactionBuilder


class DelegateRegistration(BaseTransactionBuilder):

    transaction_type = TRANSACTION_DELEGATE_REGISTRATION

    def __init__(self, username, fee=None):
        """Create a delegate registration transaction

        Args:
            username (str): username of a delegate you want to register
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()
        self.transaction.asset['delegate'] = {'username': username}
        if fee:
            self.transaction.fee = fee
