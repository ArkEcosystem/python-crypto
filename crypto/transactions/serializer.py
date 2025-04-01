from crypto.transactions.types.abstract_transaction import AbstractTransaction
from crypto.utils.transaction_utils import TransactionUtils

class Serializer:
    def __init__(self, transaction: AbstractTransaction):
        if not transaction:
            raise ValueError('No transaction data provided')
        self.transaction = transaction

    @staticmethod
    def new(transaction: AbstractTransaction):
        return Serializer(transaction)

    def serialize(self, skip_signature: bool = False) -> bytes:
        transaction_hash = TransactionUtils.to_buffer(self.transaction.data, skip_signature=skip_signature).decode()

        return bytes.fromhex(transaction_hash)
