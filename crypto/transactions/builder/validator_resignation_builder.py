from typing import Optional
from crypto.enums.contract_addresses import ContractAddresses
from crypto.transactions.builder.base import AbstractTransactionBuilder
from crypto.transactions.types.validator_resignation import ValidatorResignation

class ValidatorResignationBuilder(AbstractTransactionBuilder):
    def __init__(self, data: Optional[dict] = None):
        super().__init__(data)

        self.recipient_address(ContractAddresses.CONSENSUS.value)

    def get_transaction_instance(self, data: dict):
        return ValidatorResignation(data)
