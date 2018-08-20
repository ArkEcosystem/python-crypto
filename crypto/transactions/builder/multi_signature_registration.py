from binary.unsigned_integer.writer import write_bit8

from crypto.constants import TRANSACTION_FEES, TRANSACTION_MULTI_SIGNATURE_REGISTRATION
from crypto.transactions.builder.base import BaseTransactionBuilder


class MultiSignatureRegistrationTransaction(BaseTransactionBuilder):

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
        transaction_fee = fee or TRANSACTION_FEES[self.transaction_type]
        self.transaction.fee = (len(keysgroup) + 1) * transaction_fee

    def handle_transaction_type(self, bytes_data):
        bytes_data += write_bit8(self.transaction.asset['multisignature']['min'])
        bytes_data += write_bit8(self.transaction.asset['multisignature']['lifetime'])
        bytes_data += ''.join(self.transaction.asset['multisignature']['keysgroup']).encode()
        return bytes_data
