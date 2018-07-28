from crypto.constants import TRANSACTION_FEES, TRANSACTION_VOTE
from crypto.transactions.builder.base import BaseTransactionBuilder


class VoteTransaction(BaseTransactionBuilder):

    transaction_type = TRANSACTION_VOTE

    def __init__(self, vote, fee=None):
        """Summary

        Args:
            vote (str): address of a delegate you want to vote
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()
        self.transaction.asset['votes'] = [vote]
        self.transaction.fee = fee or TRANSACTION_FEES[self.transaction_type]

    def handle_transaction_type(self, bytes_data):
        bytes_data += ''.join(self.transaction.asset['votes']).encode()
        return bytes_data
