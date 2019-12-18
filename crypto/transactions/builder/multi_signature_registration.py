from crypto.constants import TRANSACTION_FEES, TRANSACTION_MULTI_SIGNATURE_REGISTRATION
from crypto.transactions.builder.base import BaseTransactionBuilder


class MultiSignatureRegistration(BaseTransactionBuilder):

    transaction_type = TRANSACTION_MULTI_SIGNATURE_REGISTRATION

    def __init__(self, fee=None):
        """Create a new multi signature transaction

        Args:
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        self.transaction.asset = {
            'multiSignature': {
                'min': None,
                'publicKeys': [],
            },
        }

        if fee:
            self.transaction.fee = fee

    def set_min(self, minimum_participants):
        self.transaction.asset['multiSignature']['min'] = minimum_participants

    def set_public_keys(self, public_keys):
        self.transaction.asset['multiSignature']['publicKeys'] = public_keys
        self.transaction.fee = (len(public_keys) + 1) * self.transaction.fee

    def add_participant(self, public_key):
        self.transaction.asset['multiSignature']['publicKeys'].append(public_key)
        self.transaction.fee = (len(self.transaction.asset['multiSignature']['publicKeys']) + 1) * \
            TRANSACTION_FEES.get(TRANSACTION_MULTI_SIGNATURE_REGISTRATION)
