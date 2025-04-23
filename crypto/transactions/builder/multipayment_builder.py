from crypto.enums.contract_addresses import ContractAddresses
from crypto.transactions.builder.abstract_transaction_builder import AbstractTransactionBuilder
from crypto.transactions.types.multipayment import Multipayment

class MultipaymentBuilder(AbstractTransactionBuilder):
    def __init__(self, data: dict):
        super().__init__(data)

        self.transaction.data['pay'] = [[], []]

        self.to(ContractAddresses.MULTIPAYMENT.value)
        self.transaction.refresh_payload_data()

    def pay(self, address: str, value: str):
        self.transaction.data['pay'][0].append(address)
        self.transaction.data['pay'][1].append(value)

        self.transaction.refresh_payload_data()

        self.transaction.data['value'] = str(int(self.transaction.data['value']) + int(value))

        return self

    def get_transaction_instance(self, data: dict):
        return Multipayment(data)
