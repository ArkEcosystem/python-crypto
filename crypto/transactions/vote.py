from crypto.constants import TRANSACTION_VOTE, TRANSACTION_FEES
from crypto.transactions.base import BaseTransaction


class VoteTransaction(BaseTransaction):

    transaction_type = TRANSACTION_VOTE

    def __init__(self, vote, fee=None):
        """Summary

        Args:
            vote (str): address of a delegate you want to vote
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()
        self.asset['votes'] = [vote]
        self.fee = fee or TRANSACTION_FEES[self.transaction_type]

    def handle_transaction_type(self, bytes_data):
        bytes_data += ''.join(self.asset['votes']).encode()
        return bytes_data
