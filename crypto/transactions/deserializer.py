from crypto.transactions.types.abstract_transaction import AbstractTransaction
from crypto.transactions.types.transfer import Transfer
# from crypto.transactions.types.evm_call import EvmCall
# from crypto.transactions.types.vote import Vote
# from crypto.transactions.types.unvote import Unvote
# from crypto.transactions.types.validator_registration import ValidatorRegistration
# from crypto.transactions.types.validator_resignation import ValidatorResignation
from binascii import unhexlify, hexlify

from binary.unsigned_integer.reader import (
    read_bit8,
    read_bit32,
    read_bit64,
)
# from crypto.enums.abi_function import AbiFunction  # TODO: Implement or import AbiFunction
# from crypto.utils.abi_decoder import AbiDecoder  # TODO: Implement or import AbiDecoder


class Deserializer:
    SIGNATURE_SIZE = 64
    RECOVERY_SIZE = 1

    def __init__(self, serialized: str):
        self.serialized = unhexlify(serialized) if isinstance(serialized, str) else serialized
        self.pointer = 0

    @staticmethod
    def new(serialized: str):
        return Deserializer(serialized)

    def deserialize(self) -> AbstractTransaction:
        data = {}

        self.deserialize_common(data)
        self.deserialize_data(data)
        transaction = self.guess_transaction_from_data(data)
        self.deserialize_signatures(data)

        transaction.data = data
        transaction.recover_sender()

        transaction.data['id'] = transaction.hash(skip_signature=False).hex()

        return transaction

    def read_bytes(self, length: int) -> bytes:
        result = self.serialized[self.pointer:self.pointer + length]
        self.pointer += length
        return result

    def deserialize_common(self, data: dict):
        data['network'], _ = read_bit8(self.serialized, self.pointer)
        self.pointer += 1

        nonce, _ = read_bit64(self.serialized, self.pointer)
        data['nonce'] = str(nonce)
        self.pointer += 8

        gas_price, _ = read_bit32(self.serialized, self.pointer)
        data['gasPrice'] = gas_price
        self.pointer += 4

        gas_limit, _ = read_bit32(self.serialized, self.pointer)
        data['gasLimit'] = gas_limit
        self.pointer += 4

        data['value'] = '0'

    def deserialize_data(self, data: dict):
        value = int.from_bytes(self.serialized[self.pointer:self.pointer + 32], byteorder='big')
        self.pointer += 32
        
        data['value'] = str(value)
        self.pointer += 32

        recipient_marker, _ = read_bit8(self.serialized, self.pointer)
        self.pointer += 1

        if recipient_marker == 1:
            recipient_address_bytes = self.read_bytes(20)
            recipient_address = '0x' + hexlify(recipient_address_bytes).decode()
            data['recipientAddress'] = recipient_address

        payload_length, _ = read_bit32(self.serialized, self.pointer)
        self.pointer += 4

        payload_hex = ''
        if payload_length > 0:
            payload_bytes = self.read_bytes(payload_length)
            payload_hex = hexlify(payload_bytes).decode()

        data['data'] = payload_hex

    def deserialize_signatures(self, data: dict):
        signature_length = self.SIGNATURE_SIZE + self.RECOVERY_SIZE
        signature_bytes = self.read_bytes(signature_length)
        data['signature'] = hexlify(signature_bytes).decode()

    def guess_transaction_from_data(self, data: dict) -> AbstractTransaction:
        if data['value'] != '0':
            return Transfer(data)

        # payload_data = self.decode_payload(data)
        payload_data = None  # As AbiDecoder is not implemented

        if payload_data is None:
            return Transfer(data)  # Using Transfer for now

        # if function_name == AbiFunction.VOTE.value:
        #     return Vote(data)
        # elif function_name == AbiFunction.UNVOTE.value:
        #     return Unvote(data)
        # elif function_name == AbiFunction.VALIDATOR_REGISTRATION.value:
        #     return ValidatorRegistration(data)
        # elif function_name == AbiFunction.VALIDATOR_RESIGNATION.value:
        #     return ValidatorResignation(data)
        # else:
        #     return Transfer(data)

    # def decode_payload(self, data: dict) -> dict:
    #     payload = data.get('data', '')
    #
    #     if payload == '':
    #         return None
    #
    #     return AbiDecoder().decode_function_data(payload)
