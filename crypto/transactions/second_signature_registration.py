from binascii import hexlify

from crypto.constants import TRANSACTION_FEES, TRANSACTION_SECOND_SIGNATURE_REGISTRATION
from crypto.identity.keys import public_key_from_passphrase
from crypto.transactions.base import Transaction


class SecondSignatureRegistrationTransaction(Transaction):

    transaction_type = TRANSACTION_SECOND_SIGNATURE_REGISTRATION

    def __init__(self, second_passphrase, fee=None):
        """Create a second signature registration transaction

        Args:
            second_passphrase (str): used for signing a transaction the 2nd time
            fee (int, optional): fee used for the transaction (default is already set)
        """
        super().__init__()
        public_key = public_key_from_passphrase(second_passphrase)
        self.asset['signature'] = {'publicKey': public_key}
        self.fee = fee or TRANSACTION_FEES[self.transaction_type]

    def handle_transaction_type(self, bytes_data):
        public_key = self.asset['signature']['publicKey']
        bytes_data += hexlify(public_key)
        return bytes_data
