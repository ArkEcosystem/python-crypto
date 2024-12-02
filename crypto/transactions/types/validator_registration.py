from crypto.transactions.types.abstract_transaction import AbstractTransaction
from crypto.utils.abi_encoder import AbiEncoder
from crypto.enums.abi_function import AbiFunction

class ValidatorRegistration(AbstractTransaction):
    def __init__(self, data: dict = None):
        data = data or {}
        payload = self.decode_payload(data)
        if payload:
            data['validatorPublicKey'] = payload.get('args', [None])[0].lstrip('0x') if payload.get('args') else None
        super().__init__(data)

    def get_payload(self) -> str:
        if 'validatorPublicKey' not in self.data:
            return ''
        encoder = AbiEncoder()
        return encoder.encode_function_call(AbiFunction.VALIDATOR_REGISTRATION.value, ['0x' + self.data['validatorPublicKey']])