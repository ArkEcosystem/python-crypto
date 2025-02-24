from typing import Optional
from crypto.transactions.types.abstract_transaction import AbstractTransaction
from crypto.utils.abi_encoder import AbiEncoder
from crypto.enums.abi_function import AbiFunction
from crypto.utils.transaction_utils import TransactionUtils

class ValidatorRegistration(AbstractTransaction):
    def __init__(self, data: Optional[dict] = None, payload: Optional[dict] = None):
        data = data or {}

        if payload is None:
            payload = self.decode_payload(data)

        if payload:
            data['validatorPublicKey'] = TransactionUtils.parse_hex_from_str(payload.get('args', [None])[0]) if payload.get('args') else None
        super().__init__(data)

    def get_payload(self) -> str:
        if 'validatorPublicKey' not in self.data:
            return ''
        encoder = AbiEncoder()
        return encoder.encode_function_call(AbiFunction.VALIDATOR_REGISTRATION.value, ['0x' + self.data['validatorPublicKey']])
