from crypto.transactions.types.abstract_transaction import AbstractTransaction
from crypto.utils.abi_encoder import AbiEncoder
from crypto.utils.abi_decoder import AbiDecoder

class Vote(AbstractTransaction):
    def __init__(self, data: dict = None):
        super().__init__(data)
        self.decode_payload(data)

    def get_payload(self) -> str:
        if 'vote' not in self.data:
            return ''
        encoder = AbiEncoder()
        return encoder.encode_function_call('vote', [self.data['vote']])

    def decode_payload(self, data: dict) -> dict:
        if 'data' not in data or not data['data']:
            return {}
        decoder = AbiDecoder()
        decoded = decoder.decode_function_data(data['data'])
        if decoded['functionName'] == 'vote':
            self.data['vote'] = decoded['args'][0]
        return self.data