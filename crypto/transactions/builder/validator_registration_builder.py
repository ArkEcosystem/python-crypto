from crypto.enums.contract_addresses import ContractAddresses
from crypto.transactions.builder.base import AbstractTransactionBuilder
from crypto.transactions.types.validator_registration import ValidatorRegistration

class ValidatorRegistrationBuilder(AbstractTransactionBuilder):
    def __init__(self, data: dict):
        super().__init__(data)

        self.recipient_address(ContractAddresses.CONSENSUS.value)

    def validator_public_key(self, validator_public_key: str):
        self.transaction.data['validatorPublicKey'] = validator_public_key
        self.transaction.refresh_payload_data()
        return self

    def get_transaction_instance(self, data: dict):
        return ValidatorRegistration(data)
