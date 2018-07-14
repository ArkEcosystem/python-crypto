from crypto.constants import TRANSACTION_FEES, TRANSACTION_TRANSFER
from crypto.transactions.base import BaseTransaction


class TransferTransaction(BaseTransaction):

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
        self.recipient_id = recipient_id
        self.amount = amount
        self.vendor_field = vendor_field
        self.fee = fee or TRANSACTION_FEES[self.transaction_type]

    def handle_transaction_type(self, bytes_data):
        # we do not need to handle any
        return bytes_data
