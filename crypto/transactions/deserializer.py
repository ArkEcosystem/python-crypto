from binascii import unhexlify
from typing import Optional
from crypto.configuration.network import Network
from crypto.enums.contract_abi_type import ContractAbiType
from crypto.transactions.types.abstract_transaction import AbstractTransaction
from crypto.transactions.types.multipayment import Multipayment
from crypto.transactions.types.transfer import Transfer
from crypto.transactions.types.evm_call import EvmCall
from crypto.transactions.types.username_registration import UsernameRegistration
from crypto.transactions.types.username_resignation import UsernameResignation
from crypto.transactions.types.vote import Vote
from crypto.transactions.types.unvote import Unvote
from crypto.transactions.types.validator_registration import ValidatorRegistration
from crypto.transactions.types.validator_resignation import ValidatorResignation
from crypto.transactions.types.validator_update import ValidatorUpdate

from crypto.enums.abi_function import AbiFunction
from crypto.utils.abi_decoder import AbiDecoder
from crypto.utils.rlp_decoder import RlpDecoder
from crypto.utils.transaction_utils import TransactionUtils

class Deserializer:
    SIGNATURE_SIZE = 64
    RECOVERY_SIZE = 1

    def __init__(self, serialized: str):
        self.serialized = unhexlify(serialized) if isinstance(serialized, str) else serialized
        self.pointer = 0

        self.encoded_rlp = '0x' + serialized

    @staticmethod
    def new(serialized: str):
        return Deserializer(serialized)

    def deserialize(self) -> AbstractTransaction:
        decoded_rlp = RlpDecoder.decode(self.encoded_rlp)

        data = {
            'nonce': Deserializer.__parse_big_number(decoded_rlp[0]),
            'gasPrice': Deserializer.__parse_number(decoded_rlp[1]),
            'gasLimit': Deserializer.__parse_number(decoded_rlp[2]),
            'to': Deserializer.__parse_address(decoded_rlp[3]),
            'value': Deserializer.__parse_big_number(decoded_rlp[4]),
            'data': Deserializer.__parse_hex(decoded_rlp[5]),
        }

        if len(decoded_rlp) >= 9:
            data['v'] = Deserializer.__parse_number(decoded_rlp[6]) - (Network.get_network().chain_id() * 2 + 35)
            data['r'] = Deserializer.__parse_hex(decoded_rlp[7])
            data['s'] = Deserializer.__parse_hex(decoded_rlp[8])

        transaction = self.__guess_transaction_from_data(data)

        transaction.data = data
        transaction.recover_sender()

        transaction.data['hash'] = transaction.get_id()

        return transaction

    @staticmethod
    def decode_payload(data: dict, abi_type: ContractAbiType = ContractAbiType.CONSENSUS) -> Optional[dict]:
        payload = data.get('data', '')

        if payload == '':
            return None

        decoder = AbiDecoder(abi_type)
        try:
            return decoder.decode_function_data(payload)
        except Exception as e:
            print(f"Error decoding payload: {str(e)}")

        return None

    def __guess_transaction_from_data(self, data: dict) -> AbstractTransaction:
        multipayment_payload_data = self.decode_payload(data, ContractAbiType.MULTIPAYMENT)
        if multipayment_payload_data is not None:
            function_name = multipayment_payload_data.get('functionName')
            if function_name == AbiFunction.MULTIPAYMENT.value:
                return Multipayment(data)

        consensus_payload_data = self.decode_payload(data)
        if consensus_payload_data is not None:
            function_name = consensus_payload_data.get('functionName')
            if function_name == AbiFunction.VOTE.value:
                return Vote(data)

            if function_name == AbiFunction.UNVOTE.value:
                return Unvote(data)

            if function_name == AbiFunction.VALIDATOR_REGISTRATION.value:
                return ValidatorRegistration(data)

            if function_name == AbiFunction.VALIDATOR_RESIGNATION.value:
                return ValidatorResignation(data)

            if function_name == AbiFunction.UPDATE_VALIDATOR.value:
                return ValidatorUpdate(data)

        username_payload_data = self.decode_payload(data, ContractAbiType.USERNAMES)
        if username_payload_data is not None:
            function_name = username_payload_data.get('functionName')
            if function_name == AbiFunction.USERNAME_REGISTRATION.value:
                return UsernameRegistration(data)

            if function_name == AbiFunction.USERNAME_RESIGNATION.value:
                return UsernameResignation(data)

        if data['value'] != '0':
            return Transfer(data)

        return EvmCall(data)

    @staticmethod
    def __parse_number(value: str) -> int:
        return 0 if value == '0x' else int(value, 16)

    @staticmethod
    def __parse_big_number(value: str) -> str:
        return str(Deserializer.__parse_number(value))

    @staticmethod
    def __parse_hex(value: str) -> str:
        return TransactionUtils.parse_hex_from_str(value)

    @staticmethod
    def __parse_address(value: str) -> Optional[str]:
        return None if value == '0x' else value
