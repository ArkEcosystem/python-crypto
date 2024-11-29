# crypto/utils/abi_base.py

import json
import os
import re
from binascii import unhexlify
from Cryptodome.Hash import keccak
from crypto.identity.address import get_checksum_address


class AbiBase:
    def __init__(self):
        # Cargar el ABI desde un archivo JSON
        abi_file_path = os.path.join(os.path.dirname(__file__), 'Abi.Consensus.json')
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
        computed_checksum_address = get_checksum_address(address.lower())
        return address == computed_checksum_address

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
