from crypto.identity.private_key import PrivateKey
from crypto.transactions.types.abstract_transaction import AbstractTransaction


class AbstractTransactionBuilder:
    def __init__(self, data: dict):
        data = {
            'value': 0,
            'senderPublicKey': '',
            'gasPrice': '5',
            'gasLimit': 1_000_000,
            'nonce': '1',
            'data': '',

            **data,
        }

        self.transaction = self.get_transaction_instance(data)

    def __str__(self):
        return self.to_json()

    @classmethod
    def new(cls):
        return cls({})

    def gas_limit(self, gas_limit: int):
        self.transaction.data['gasLimit'] = int(gas_limit)
        return self

    def to(self, to: str):
        self.transaction.data['to'] = to
        return self

    def gas_price(self, gas_price: int):
        self.transaction.data['gasPrice'] = int(gas_price)
        return self

    def nonce(self, nonce: str):
        self.transaction.data['nonce'] = nonce
        return self

    def sign(self, passphrase: str):
        keys = PrivateKey.from_passphrase(passphrase)
        self.transaction.data['senderPublicKey'] = keys.public_key
        self.transaction = self.transaction.sign(keys)
        self.transaction.data['hash'] = self.transaction.get_id()
        return self

    def legacy_second_sign(self, passphrase: str, second_passphrase: str):
        self.sign(passphrase)

        self.transaction.legacy_second_sign(PrivateKey.from_passphrase(second_passphrase))

        return self

    def verify(self):
        return self.transaction.verify()

    def to_dict(self):
        return self.transaction.to_dict()

    def to_json(self):
        return self.transaction.to_json()

    def get_transaction_instance(self, data: dict) -> AbstractTransaction:
        raise NotImplementedError("Subclasses must implement get_transaction_instance()")
