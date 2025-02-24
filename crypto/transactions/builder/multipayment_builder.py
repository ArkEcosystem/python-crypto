from typing import Optional
from crypto.enums.contract_addresses import ContractAddresses
from crypto.transactions.builder.base import AbstractTransactionBuilder
from crypto.transactions.types.multipayment import Multipayment

class MultipaymentBuilder(AbstractTransactionBuilder):
    def __init__(self, data: Optional[dict] = None):
        super().__init__(data)

        self.transaction.data['pay'] = [[], []]

        self.recipient_address(ContractAddresses.MULTIPAYMENT.value)
        self.transaction.refresh_payload_data()

    def pay(self, address: str, amount: str):
        self.transaction.data['pay'][0].append(address)
        self.transaction.data['pay'][1].append(amount)

        self.transaction.refresh_payload_data()

        self.transaction.data['value'] = str(int(self.transaction.data['value']) + int(amount))

        return self

    def get_transaction_instance(self, data: dict):
        return Multipayment(data)
