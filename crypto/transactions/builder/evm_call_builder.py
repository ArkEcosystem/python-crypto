from crypto.transactions.builder.base import AbstractTransactionBuilder
from crypto.transactions.types.evm_call import EvmCall

class EvmCallBuilder(AbstractTransactionBuilder):
    def payload(self, payload: str):
        payload = payload.lstrip('0x')  # Remove '0x' prefix if present
        self.transaction.data['data'] = payload
        return self

    def get_transaction_instance(self, data: dict):
        return EvmCall(data)