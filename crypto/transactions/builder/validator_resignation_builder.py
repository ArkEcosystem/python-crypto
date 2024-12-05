from crypto.transactions.builder.base import AbstractTransactionBuilder
from crypto.transactions.types.validator_resignation import ValidatorResignation

class ValidatorResignationBuilder(AbstractTransactionBuilder):
    def get_transaction_instance(self, data: dict):
        return ValidatorResignation(data)