from crypto.constants import TRANSACTION_DELEGATE_REGISTRATION
from crypto.identity.public_key import PublicKey
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

    def sign(self, passphrase):
        public_key = PublicKey.from_passphrase(passphrase)
        self.transaction.asset['delegate']['publicKey'] = public_key
        super().sign(passphrase)
