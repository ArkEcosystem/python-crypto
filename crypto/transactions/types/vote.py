from typing import Optional
from crypto.transactions.types.abstract_transaction import AbstractTransaction
from crypto.utils.abi_encoder import AbiEncoder
from crypto.enums.abi_function import AbiFunction

class Vote(AbstractTransaction):
    def __init__(self, data: Optional[dict] = None):
        data = data or {}
        payload = self.decode_payload(data)
        if payload:
            data['vote'] = payload.get('args', [None])[0] if payload.get('args') else None

        super().__init__(data)

    def get_payload(self) -> str:
        if 'vote' not in self.data:
            return ''
        encoder = AbiEncoder()
        return encoder.encode_function_call(AbiFunction.VOTE.value, [self.data['vote']])
