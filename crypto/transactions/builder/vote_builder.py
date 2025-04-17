from crypto.enums.contract_addresses import ContractAddresses
from crypto.transactions.builder.base import AbstractTransactionBuilder
from crypto.transactions.types.vote import Vote

class VoteBuilder(AbstractTransactionBuilder):
    def __init__(self, data: dict):
        super().__init__(data)

        self.to(ContractAddresses.CONSENSUS.value)

    def vote(self, vote: str):
        self.transaction.data['vote'] = vote
        self.transaction.refresh_payload_data()
        return self

    def get_transaction_instance(self, data: dict) -> Vote:
        return Vote(data)
