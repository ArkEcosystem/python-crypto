from crypto.constants import TRANSACTION_DELEGATE_REGISTRATION, TRANSACTION_FEES
from crypto.transactions.base import Transaction


class DelegateRegistrationTransaction(Transaction):

    transaction_type = TRANSACTION_DELEGATE_REGISTRATION

    def __init__(self, username, fee=None):
        """Create a delegate registration transaction

        Args:
            username (str): username of a delegate you want to register
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()
        self.asset['delegate'] = {'username': username}
        self.fee = fee or TRANSACTION_FEES[self.transaction_type]

    def handle_transaction_type(self, bytes_data):
        bytes_data += self.asset['delegate']['username']
        return bytes_data
