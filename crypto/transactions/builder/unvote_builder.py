from crypto.transactions.builder.base import AbstractTransactionBuilder
from crypto.transactions.types.unvote import Unvote

class UnvoteBuilder(AbstractTransactionBuilder):
    def get_transaction_instance(self, data: dict):
        return Unvote(data)