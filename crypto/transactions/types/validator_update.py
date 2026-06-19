from crypto.transactions.types.abstract_transaction import AbstractTransaction
from crypto.utils.abi_encoder import AbiEncoder
from crypto.enums.abi_function import AbiFunction


class ValidatorUpdate(AbstractTransaction):
    def __init__(self, data: dict):
        payload = self._decode_payload(data)
        if payload:
            data['validatorPublicKey'], data['validatorProof'] = payload['args']

        super().__init__(data)

    def get_payload(self) -> str:
        if 'validatorPublicKey' not in self.data or 'validatorProof' not in self.data:
            return ''
        encoder = AbiEncoder()
        return encoder.encode_function_call(
            AbiFunction.UPDATE_VALIDATOR.value,
            [self.data['validatorPublicKey'], self.data['validatorProof']],
        )
