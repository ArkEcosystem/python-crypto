from crypto.transactions.types.abstract_transaction import AbstractTransaction
from crypto.utils.abi_encoder import AbiEncoder
from crypto.enums.abi_function import AbiFunction

class ValidatorResignation(AbstractTransaction):
    def get_payload(self) -> str:
        encoder = AbiEncoder()
        return encoder.encode_function_call(AbiFunction.VALIDATOR_RESIGNATION.value)