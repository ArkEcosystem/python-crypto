from crypto.transactions.builder.abstract_transaction_builder import AbstractTransactionBuilder
from crypto.transactions.types.evm_call import EvmCall
from crypto.utils.transaction_utils import TransactionUtils

class EvmCallBuilder(AbstractTransactionBuilder):
    def payload(self, payload: str):
        payload = TransactionUtils.parse_hex_from_str(payload)  # Remove '0x' prefix if present

        self.transaction.data['data'] = payload

        return self

    def get_transaction_instance(self, data: dict):
        return EvmCall(data)
