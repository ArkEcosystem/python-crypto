from crypto.constants import TRANSACTION_MULTI_SIGNATURE_REGISTRATION
from crypto.transactions.builder.base import BaseTransactionBuilder


class MultiSignatureRegistration(BaseTransactionBuilder):

    transaction_type = TRANSACTION_MULTI_SIGNATURE_REGISTRATION

    def __init__(self, min_signatures, lifetime, keysgroup, fee=None):
        """Create a new multi signature transaction

        Args:
            min_signatures (int): minimum required signatures
            lifetime (int): transaction lifetime
            keysgroup (list): list of signatures required
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()
        self.transaction.asset = {
            'multisignature': {
                'min': min_signatures,
                'lifetime': lifetime,
                'keysgroup': keysgroup,
            },
        }
        # default transaction fee for this type i set in the base builder
        transaction_fee = fee or self.transaction.fee
        self.transaction.fee = (len(keysgroup) + 1) * transaction_fee
