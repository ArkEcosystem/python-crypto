# crypto/utils/abi_base.py

import json
import os
import re
from typing import Optional
from Cryptodome.Hash import keccak
from crypto.enums.contract_abi_type import ContractAbiType
from crypto.identity.address import Address


class AbiBase:
    def __init__(self, abi_type: ContractAbiType = ContractAbiType.CONSENSUS, path: Optional[str] = None):
        abi_file_path = self.__contract_abi_path(abi_type, path)

        if abi_file_path is None:
            raise Exception('ABI file path is not provided')

        with open(abi_file_path, 'r') as f:
            abi_json = json.load(f)

        self.abi = abi_json.get('abi', [])

    def get_array_components(self, type_str):
        match = re.match(r'^(.*)\[(\d*)\]$', type_str)
        if match:
            inner_type = match.group(1)
            length_str = match.group(2)
            length = int(length_str) if length_str != '' else None
            return length, inner_type
        return None

    def strip_hex_prefix(self, hex_str):
        if hex_str.startswith('0x') or hex_str.startswith('0X'):
            return hex_str[2:]
        return hex_str

    def is_valid_address(self, address):
        # Compute the checksum address and compare
        computed_checksum_address = Address.get_checksum_address(address.lower())

        return address.lower() == computed_checksum_address.lower()

    def keccak256(self, input_str):
        k = keccak.new(digest_bits=256)
        k.update(input_str.encode('utf-8'))
        return '0x' + k.hexdigest()

    def get_function_signature(self, abi_item):
        name = abi_item['name']
        inputs = abi_item.get('inputs', [])
        types = [input_item['type'] for input_item in inputs]
        return f"{name}({','.join(types)})"

    def to_function_selector(self, abi_item):
        signature = self.get_function_signature(abi_item)
        hash_ = self.keccak256(signature)
        selector = '0x' + self.strip_hex_prefix(hash_)[0:8]
        return selector

    def __contract_abi_path(self, abi_type: ContractAbiType, path: Optional[str] = None) -> Optional[str]:
        if abi_type == ContractAbiType.CONSENSUS:
            return os.path.join(os.path.dirname(__file__), 'abi/json', 'Abi.Consensus.json')

        if abi_type == ContractAbiType.MULTIPAYMENT:
            return os.path.join(os.path.dirname(__file__), 'abi/json', 'Abi.Multipayment.json')

        if abi_type == ContractAbiType.TOKEN:
            return os.path.join(os.path.dirname(__file__), 'abi/json', 'Abi.Token.json')

        if abi_type == ContractAbiType.USERNAMES:
            return os.path.join(os.path.dirname(__file__), 'abi/json', 'Abi.Usernames.json')

        if abi_type == ContractAbiType.ERC20BATCH_TRANSFER:
            return os.path.join(os.path.dirname(__file__), 'abi/json', 'Abi.ERC20BatchTransfer.json')

        return path
