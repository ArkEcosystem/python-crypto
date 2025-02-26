from crypto.transactions.builder.base import AbstractTransactionBuilder
from crypto.transactions.types.transfer import Transfer


class TransferBuilder(AbstractTransactionBuilder):
    def value(self, value: int):
        self.transaction.data['value'] = int(value)
        self.transaction.refresh_payload_data()
        return self

    def get_transaction_instance(self, data: dict):
        return Transfer(data)
