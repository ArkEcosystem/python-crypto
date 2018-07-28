from crypto.constants import TRANSACTION_FEES, TRANSACTION_TRANSFER
from crypto.transactions.builder.base import BaseTransactionBuilder


class TransferBuilder(BaseTransactionBuilder):

    transaction_type = TRANSACTION_TRANSFER

    def __init__(self, recipient_id, amount, vendor_field=None, fee=None):
        """Create a transfer transaction

        Args:
            recipient_id (str): address to which you want to send coins
            amount (int): amount of coins you want to transfer
            vendor_field (str): value for the vendor field aka smartbridge
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()
        self.transaction.recipient_id = recipient_id
        self.transaction.amount = amount
        self.transaction.vendor_field = vendor_field
        self.transaction.fee = fee or TRANSACTION_FEES[self.transaction_type]
