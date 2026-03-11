from crypto.enums.abi_function import AbiFunction
from crypto.enums.contract_abi_type import ContractAbiType
from crypto.transactions.builder.abstract_transaction_builder import (
    AbstractTransactionBuilder,
)
from crypto.transactions.types.evm_call import EvmCall
from crypto.utils.abi_encoder import AbiEncoder
from crypto.utils.transaction_utils import TransactionUtils


class TokenApproveBuilder(AbstractTransactionBuilder):
    def contract_address(self, address):
        self.transaction.data['to'] = address
        return self

    def spender(self, address, amount):
        encoder = AbiEncoder(ContractAbiType.TOKEN)
        payload = encoder.encode_function_call(
            AbiFunction.APPROVE.value, [address, amount]
        )
        self.transaction.data['data'] = TransactionUtils.parse_hex_from_str(
            payload
        )
        return self

    def get_transaction_instance(self, data):
        return EvmCall(data)
