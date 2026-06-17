from crypto.enums.contract_addresses import ContractAddresses
from crypto.identity.proof_of_possession import ProofOfPossession
from crypto.transactions.builder.abstract_transaction_builder import AbstractTransactionBuilder
from crypto.transactions.types.validator_update import ValidatorUpdate


class ValidatorUpdateBuilder(AbstractTransactionBuilder):
    def __init__(self, data: dict):
        super().__init__(data)
        self.to(ContractAddresses.CONSENSUS.value)

    def validator_passphrase(self, passphrase: str):
        bls = ProofOfPossession.from_passphrase(passphrase)
        self.transaction.data['validatorPublicKey'] = '0x' + bls['pk']
        self.transaction.data['validatorProof']     = '0x' + bls['pop']
        self.transaction.refresh_payload_data()
        return self

    def get_transaction_instance(self, data: dict):
        return ValidatorUpdate(data)
