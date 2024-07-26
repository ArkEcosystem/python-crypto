from crypto.constants import TRANSACTION_VOTE
from crypto.identity.address import address_from_passphrase
from crypto.transactions.builder.base import BaseTransactionBuilder


class Vote(BaseTransactionBuilder):
    transaction_type = TRANSACTION_VOTE

    def __init__(self, votes: list[str] | None, unvotes: list[str] | None, fee: int | None = None):
        """Create a vote transaction

        Args:
            vote (str, optional): address of a delegate you want to vote
            unvote (str, optional): address of a delegate you want to unvote
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        self.transaction.asset['votes'] = votes if votes else []
        self.transaction.asset['unvotes'] = unvotes if unvotes else []

        if fee:
            self.transaction.fee = fee

    def sign(self, passphrase):
        self.transaction.recipientId = address_from_passphrase(passphrase)
        super().sign(passphrase)
