from crypto.transactions.types.abstract_transaction import AbstractTransaction

class EvmCall(AbstractTransaction):
    def get_payload(self) -> str:
        return self.data.get('data', '')