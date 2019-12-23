from crypto.constants import TRANSACTION_TRANSFER
from crypto.transactions.builder.base import BaseTransactionBuilder


class Transfer(BaseTransactionBuilder):

    transaction_type = TRANSACTION_TRANSFER

    def __init__(self, recipientId, amount, vendorField=None, fee=None):
        """Create a transfer transaction

        Args:
            recipientId (str): address to which you want to send coins
            amount (int): amount of coins you want to transfer
            vendorField (str): value for the vendor field aka smartbridge
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        self.transaction.recipientId = recipientId

        if type(amount) == int and amount > 0:
            self.transaction.amount = amount
        else:
            raise ValueError('Amount is not valid')

        self.transaction.vendorField = vendorField.encode() if vendorField else None

        if fee:
            self.transaction.fee = fee
