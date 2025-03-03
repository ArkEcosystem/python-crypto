from typing import Optional
from crypto.enums.contract_abi_type import ContractAbiType
from crypto.transactions.types.abstract_transaction import AbstractTransaction
from crypto.utils.abi_encoder import AbiEncoder
from crypto.enums.abi_function import AbiFunction

class UsernameRegistration(AbstractTransaction):
    def __init__(self, data: dict):
        payload = self.decode_payload(data, ContractAbiType.USERNAMES)
        if payload:
            data['username'] = payload.get('args', [None])[0] if payload.get('args') else None

        super().__init__(data)

    def get_payload(self) -> str:
        if 'username' not in self.data:
            return ''

        encoder = AbiEncoder(ContractAbiType.USERNAMES)

        return encoder.encode_function_call(AbiFunction.USERNAME_REGISTRATION.value, [self.data['username']])
