from crypto.constants import TRANSACTION_HTLC_LOCK, TRANSACTION_TYPE_GROUP
from crypto.transactions.builder.base import BaseTransactionBuilder


class HtlcLock(BaseTransactionBuilder):

    transaction_type = TRANSACTION_HTLC_LOCK

    def __init__(self, recipient_id, secret_hash, expiration_type, expiration_value, vendorField=None, fee=None):
        """Create a timelock transaction

        Args:
            recipient_id (str): recipient identifier
            secret_hash (str): a hash of the secret. The SAME hash must be used in the corresponding “claim” transaction
            expiration_type (int): type of the expiration. Either block height or network epoch timestamp based
            expiration_value (int): Expiration of transaction in seconds or height depending on expiration_type
            vendorField (str): value for the vendor field aka smartbridge
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        self.transaction.recipientId = recipient_id

        self.transaction.typeGroup = self.get_type_group()

        self.transaction.asset['lock'] = {
            'secretHash': secret_hash,
            'expiration': {
                'type': expiration_type,
                'value': expiration_value
            }
        }

        self.transaction.vendorField = vendorField.encode() if vendorField else None

        if fee:
            self.transaction.fee = fee

    def get_type_group(self):
        return TRANSACTION_TYPE_GROUP.CORE.value
