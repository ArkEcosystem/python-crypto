from crypto.constants import TRANSACTION_SECOND_SIGNATURE_REGISTRATION
from crypto.identity.public_key import PublicKey
from crypto.transactions.builder.base import BaseTransactionBuilder


class SecondSignatureRegistration(BaseTransactionBuilder):

    transaction_type = TRANSACTION_SECOND_SIGNATURE_REGISTRATION

    def __init__(self, second_passphrase, fee=None):
        """Create a second signature registration transaction

        Args:
            second_passphrase (str): used for signing a transaction the 2nd time
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        public_key = PublicKey.from_passphrase(second_passphrase)
        self.transaction.asset['signature'] = {'publicKey': public_key}

        if fee:
            self.transaction.fee = fee
