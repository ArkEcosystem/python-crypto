import re
from crypto.transactions.types.abstract_transaction import AbstractTransaction
from crypto.transactions.types.transfer import Transfer
from crypto.transactions.types.evm_call import EvmCall
from crypto.transactions.types.vote import Vote
from crypto.transactions.types.unvote import Unvote
from crypto.transactions.types.validator_registration import ValidatorRegistration
from crypto.transactions.types.validator_resignation import ValidatorResignation
from binascii import unhexlify

from crypto.enums.abi_function import AbiFunction
from crypto.utils.abi_decoder import AbiDecoder
from crypto.utils.rlp_decoder import RlpDecoder

class Deserializer:
    SIGNATURE_SIZE = 64
    RECOVERY_SIZE = 1
    EIP1559_PREFIX = '02'

    def __init__(self, serialized: str):
        self.serialized = unhexlify(serialized) if isinstance(serialized, str) else serialized
        self.pointer = 0

        self.encoded_rlp = '0x' + serialized[2:]

    @staticmethod
    def new(serialized: str):
        return Deserializer(serialized)

    def deserialize(self) -> AbstractTransaction:
        decoded_rlp = RlpDecoder.decode(self.encoded_rlp)

        data = {
            'network': Deserializer.parse_number(decoded_rlp[0]),
            'nonce': Deserializer.parse_big_number(decoded_rlp[1]),
            'gasPrice': Deserializer.parse_number(decoded_rlp[3]),
            'gasLimit': Deserializer.parse_number(decoded_rlp[4]),
            'recipientAddress': Deserializer.parse_address(decoded_rlp[5]),
            'value': Deserializer.parse_big_number(decoded_rlp[6]),
            'data': Deserializer.parse_hex(decoded_rlp[7]),
        }

        if len(decoded_rlp) == 12:
            data['v'] = Deserializer.parse_number(decoded_rlp[9]) + 31
            data['r'] = Deserializer.parse_hex(decoded_rlp[10])
            data['s'] = Deserializer.parse_hex(decoded_rlp[11])

        transaction = self.guess_transaction_from_data(data)

        transaction.data = data
        transaction.recover_sender()

        transaction.data['id'] = transaction.get_id()

        return transaction

    def guess_transaction_from_data(self, data: dict) -> AbstractTransaction:
        if data['value'] != '0':
            return Transfer(data)

        payload_data = self.decode_payload(data)

        if payload_data is None:
            return EvmCall(data)

        function_name = payload_data.get('functionName')
        if function_name == AbiFunction.VOTE.value:
            return Vote(data)
        elif function_name == AbiFunction.UNVOTE.value:
            return Unvote(data)
        elif function_name == AbiFunction.VALIDATOR_REGISTRATION.value:
            return ValidatorRegistration(data)
        elif function_name == AbiFunction.VALIDATOR_RESIGNATION.value:
            return ValidatorResignation(data)
        else:
            return EvmCall(data)

    def decode_payload(self, data: dict) -> dict | None:
        payload = data.get('data', '')

        if payload == '':
            return None

        decoder = AbiDecoder()
        try:
            return decoder.decode_function_data(payload)
        except Exception as e:
            print(f"Error decoding payload: {str(e)}")

        return None

    @staticmethod
    def parse_number(value: str) -> int:
        return 0 if value == '0x' else int(value, 16)

    @staticmethod
    def parse_big_number(value: str) -> str:
        return str(Deserializer.parse_number(value))

    @staticmethod
    def parse_hex(value: str) -> str:
        return re.sub(r'^0x', '', value)

    @staticmethod
    def parse_address(value: str) -> str | None:
        return None if value == '0x' else value
