from crypto.enums.contract_addresses import ContractAddresses
from crypto.transactions.builder.abstract_transaction_builder import AbstractTransactionBuilder
from crypto.transactions.types.validator_resignation import ValidatorResignation

class ValidatorResignationBuilder(AbstractTransactionBuilder):
    def __init__(self, data: dict):
        super().__init__(data)

        self.to(ContractAddresses.CONSENSUS.value)

    def get_transaction_instance(self, data: dict):
        return ValidatorResignation(data)
