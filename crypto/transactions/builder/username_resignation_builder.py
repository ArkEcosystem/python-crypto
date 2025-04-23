from crypto.enums.contract_addresses import ContractAddresses
from crypto.transactions.builder.abstract_transaction_builder import AbstractTransactionBuilder
from crypto.transactions.types.username_resignation import UsernameResignation

class UsernameResignationBuilder(AbstractTransactionBuilder):
    def __init__(self, data: dict):
        super().__init__(data)

        self.to(ContractAddresses.USERNAMES.value)

    def get_transaction_instance(self, data: dict):
        return UsernameResignation(data)
