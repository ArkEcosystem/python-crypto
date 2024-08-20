from typing import Optional

from crypto.constants import TRANSACTION_VALIDATOR_REGISTRATION
from crypto.transactions.builder.base import BaseTransactionBuilder

import sys
import os
from os.path import dirname

sys.path.append(os.path.join(dirname(dirname(dirname(__file__))), 'thirdparty/bls-signatures/python-impl'))

from ec import G1FromBytes

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
            G1FromBytes(bytes.fromhex(public_key)).check_valid()
        except Exception:
            raise ValueError('Invalid BLS public key')
