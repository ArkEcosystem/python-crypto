from crypto.constants import TRANSACTION_MULTI_SIGNATURE_REGISTRATION
from crypto.transactions.builder.base import BaseTransactionBuilder


class MultiSignatureRegistration(BaseTransactionBuilder):

    transaction_type = TRANSACTION_MULTI_SIGNATURE_REGISTRATION

    def __init__(self, min_signatures, lifetime, publickeys, fee=None):
        """Create a new multi signature transaction

        Args:
            min_signatures (int): minimum required signatures
            lifetime (int): transaction lifetime
            publickeys (list): list of signatures required
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()
        self.transaction.asset = {
            'multiSignature': {
                'min': min_signatures,
                'lifetime': lifetime,
                'publicKeys': publickeys,
            },
        }
        # default transaction fee for this type i set in the base builder
        transaction_fee = fee or self.transaction.fee
        self.transaction.fee = (len(publickeys) + 1) * transaction_fee
