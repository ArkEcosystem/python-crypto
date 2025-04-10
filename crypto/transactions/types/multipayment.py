from typing import Optional
from crypto.enums.contract_abi_type import ContractAbiType
from crypto.transactions.types.abstract_transaction import AbstractTransaction
from crypto.utils.abi_encoder import AbiEncoder
from crypto.enums.abi_function import AbiFunction

class Multipayment(AbstractTransaction):
    def __init__(self, data: dict):
        payload = self._decode_payload(data, ContractAbiType.MULTIPAYMENT)
        if payload:
            data['pay'] = payload.get('args', [])

        super().__init__(data)

    def get_payload(self) -> str:
        if 'pay' not in self.data:
            return ''

        encoder = AbiEncoder(ContractAbiType.MULTIPAYMENT)

        return encoder.encode_function_call(AbiFunction.MULTIPAYMENT.value, self.data['pay'])
