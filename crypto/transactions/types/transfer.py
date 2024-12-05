from crypto.transactions.types.abstract_transaction import AbstractTransaction


class Transfer(AbstractTransaction):
    def get_payload(self) -> str:
        return ''
