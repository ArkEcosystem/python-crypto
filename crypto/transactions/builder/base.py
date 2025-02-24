from typing import Optional

from crypto.configuration.network import get_network
from crypto.identity.private_key import PrivateKey
from crypto.transactions.types.abstract_transaction import AbstractTransaction


class AbstractTransactionBuilder:
    def __init__(self, data: Optional[dict] = None):
        default_data = {
            'value': '0',
            'senderPublicKey': '',
            'gasPrice': '5',
            'nonce': '1',
            'network': get_network()['version'],
            'gasLimit': 1_000_000,
            'data': '',
        }
        self.transaction = self.get_transaction_instance(data or default_data)

    def __str__(self):
        return self.to_json()

    @classmethod
    def new(cls, data: Optional[dict] = None):
        return cls(data)

    def gas_limit(self, gas_limit: int | str):
        self.transaction.data['gasLimit'] = gas_limit
        return self

    def recipient_address(self, recipient_address: str):
        self.transaction.data['recipientAddress'] = recipient_address
        return self

    def gas_price(self, gas_price: int | str):
        self.transaction.data['gasPrice'] = gas_price
        return self

    def nonce(self, nonce: str):
        self.transaction.data['nonce'] = nonce
        return self

    def network(self, network: int):
        self.transaction.data['network'] = network
        return self

    def sign(self, passphrase: str):
        keys = PrivateKey.from_passphrase(passphrase)
        self.transaction.data['senderPublicKey'] = keys.public_key
        self.transaction = self.transaction.sign(keys)
        self.transaction.data['id'] = self.transaction.get_id()
        return self

    def verify(self):
        return self.transaction.verify()

    def to_dict(self):
        return self.transaction.to_dict()

    def to_json(self):
        return self.transaction.to_json()

    def get_transaction_instance(self, data: dict) -> AbstractTransaction:
        raise NotImplementedError("Subclasses must implement get_transaction_instance()")
