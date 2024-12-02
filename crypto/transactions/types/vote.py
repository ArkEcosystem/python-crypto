from crypto.transactions.types.abstract_transaction import AbstractTransaction
from crypto.utils.abi_encoder import AbiEncoder

class Vote(AbstractTransaction):
    def __init__(self, data: dict = None):
        super().__init__(data)
        self.decode_payload(data)

    def get_payload(self) -> str:
        if 'vote' not in self.data:
            return ''
        encoder = AbiEncoder()
        return encoder.encode_function_call('vote', [self.data['vote']])