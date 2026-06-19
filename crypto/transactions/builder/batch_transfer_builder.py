from crypto.enums.abi_function import AbiFunction
from crypto.enums.contract_abi_type import ContractAbiType
from crypto.enums.contract_addresses import ContractAddresses
from crypto.transactions.builder.abstract_transaction_builder import (
    AbstractTransactionBuilder,
)
from crypto.transactions.types.evm_call import EvmCall
from crypto.utils.abi_encoder import AbiEncoder
from crypto.utils.transaction_utils import TransactionUtils


class BatchTransferBuilder(AbstractTransactionBuilder):
    def __init__(self, data: dict):
        super().__init__(data)

        self._token_address = None
        self._recipients = []
        self._amounts = []

        self.to(ContractAddresses.BATCH_TRANSFER.value)

    def token_address(self, token_address: str):
        self._token_address = token_address
        return self

    def add_recipient(self, address: str, amount: int):
        self._recipients.append(address)
        self._amounts.append(amount)
        return self

    def sign(self, passphrase: str):
        self._encode()
        return super().sign(passphrase)

    def _encode(self):
        if len(self._recipients) == 0:
            raise Exception('Must add at least one recipient before encoding.')

        if self._token_address is None:
            raise Exception('Must set tokenAddress before encoding.')

        encoder = AbiEncoder(ContractAbiType.ERC20BATCH_TRANSFER)
        payload = encoder.encode_function_call(
            AbiFunction.BATCH_TRANSFER_FROM.value,
            [self._token_address, self._recipients, self._amounts],
        )
        self.transaction.data['data'] = TransactionUtils.parse_hex_from_str(
            payload
        )

    def get_transaction_instance(self, data: dict):
        return EvmCall(data)
