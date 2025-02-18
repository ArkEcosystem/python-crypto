from crypto.enums.contract_abi_type import ContractAbiType
from crypto.transactions.types.abstract_transaction import AbstractTransaction
from crypto.utils.abi_encoder import AbiEncoder
from crypto.enums.abi_function import AbiFunction

class UsernameResignation(AbstractTransaction):
    def get_payload(self) -> str:
        encoder = AbiEncoder(ContractAbiType.USERNAMES)

        return encoder.encode_function_call(AbiFunction.USERNAME_RESIGNATION.value)
