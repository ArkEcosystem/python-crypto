from crypto.enums.abi_function import AbiFunction
from crypto.enums.contract_abi_type import ContractAbiType
from crypto.utils.abi_encoder import AbiEncoder


class TransactionDataEncoder:
    @staticmethod
    def multi_payment(recipients, amounts):
        return AbiEncoder(ContractAbiType.MULTIPAYMENT).encode_function_call_hex(
            AbiFunction.MULTIPAYMENT.value, [recipients, amounts]
        )

    @staticmethod
    def update_validator(validator_public_key):
        key = validator_public_key
        if not key.startswith('0x'):
            key = '0x' + key
        return AbiEncoder(ContractAbiType.CONSENSUS).encode_function_call_hex(
            AbiFunction.UPDATE_VALIDATOR.value, [key]
        )

    @staticmethod
    def username_registration(username):
        return AbiEncoder(ContractAbiType.USERNAMES).encode_function_call_hex(
            AbiFunction.USERNAME_REGISTRATION.value, [username]
        )

    @staticmethod
    def username_resignation():
        return AbiEncoder(ContractAbiType.USERNAMES).encode_function_call_hex(
            AbiFunction.USERNAME_RESIGNATION.value, []
        )

    @staticmethod
    def validator_registration(validator_public_key):
        key = validator_public_key
        if not key.startswith('0x'):
            key = '0x' + key
        return AbiEncoder(ContractAbiType.CONSENSUS).encode_function_call_hex(
            AbiFunction.VALIDATOR_REGISTRATION.value, [key]
        )

    @staticmethod
    def validator_resignation():
        return AbiEncoder(ContractAbiType.CONSENSUS).encode_function_call_hex(
            AbiFunction.VALIDATOR_RESIGNATION.value, []
        )

    @staticmethod
    def token_transfer(recipient_address, amount):
        return AbiEncoder(ContractAbiType.TOKEN).encode_function_call_hex(
            AbiFunction.TRANSFER.value, [recipient_address, amount]
        )

    @staticmethod
    def vote(vote_address):
        return AbiEncoder(ContractAbiType.CONSENSUS).encode_function_call_hex(
            AbiFunction.VOTE.value, [vote_address]
        )

    @staticmethod
    def unvote():
        return AbiEncoder(ContractAbiType.CONSENSUS).encode_function_call_hex(
            AbiFunction.UNVOTE.value, []
        )
