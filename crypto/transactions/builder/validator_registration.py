from typing import Optional

import blspy

from crypto.constants import TRANSACTION_VALIDATOR_REGISTRATION
from crypto.transactions.builder.base import BaseTransactionBuilder

class ValidatorRegistration(BaseTransactionBuilder):
    transaction_type = TRANSACTION_VALIDATOR_REGISTRATION

    def __init__(self, public_key: str, fee: Optional[int] = None):
        """Create a validator registration transaction

        Args:
            public_key (str): BLS public key of a validator you want to register
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()

        self.validate_bls_public_key(public_key)

        self.transaction.asset['validatorPublicKey'] = public_key

        if fee:
            self.transaction.fee = fee

    def validate_bls_public_key(self, public_key: str):
        """Validate BLS public key

        Args:
            public_key (str): BLS public key to validate
        """
        if len(public_key) != 96:
            raise ValueError('Invalid BLS public key')

        try:
            blspy.PublicKeyMPL.from_bytes(bytes.fromhex(public_key))
        except Exception:
            raise ValueError('Invalid BLS public key')
