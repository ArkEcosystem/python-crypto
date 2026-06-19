# crypto/utils/abi_decoder.py

from crypto.utils.abi_base import AbiBase
import binascii
import re
from crypto.identity.address import Address


class AbiDecoder(AbiBase):
    def decode_function_data(self, data):
        data = self.strip_hex_prefix(data)
        function_selector = data[:8]
        abi_item = self.find_function_by_selector(function_selector)
        if not abi_item:
            raise Exception('Function selector not found in ABI: ' + function_selector)

        encoded_params = data[8:]
        decoded_params = self.decode_abi_parameters(abi_item['inputs'], encoded_params)

        return {
            'functionName': abi_item['name'],
            'args': decoded_params,
        }

    def find_function_by_selector(self, selector):
        for item in self.abi:
            if item['type'] == 'function':
                function_signature = self.get_function_signature(item)
                function_selector = self.strip_hex_prefix(self.keccak256(function_signature))[0:8]
                if function_selector == selector:
                    return item

        return None

    def decode_abi_parameters(self, params, data):
        if not data and len(params) > 0:
            raise Exception('No data to decode')

        bytes_data = binascii.unhexlify(data)
        cursor = 0
        values = []
        for param in params:
            value, consumed = self.decode_parameter(bytes_data, cursor, param)
            cursor += consumed
            values.append(value)

        return values

    def decode_parameter(self, bytes_data, offset, param):
        type_ = param['type']
        array_components = self.get_array_components(type_)
        if array_components:
            length, base_type = array_components
            param['type'] = base_type

            return self.decode_array(bytes_data, offset, param, length)

        if type_ == 'address':
            return self.decode_address(bytes_data, offset)

        if type_ == 'bool':
            return self.decode_bool(bytes_data, offset)

        if type_ == 'string':
            return self.decode_string(bytes_data, offset)

        if type_ == 'bytes':
            return self.decode_dynamic_bytes(bytes_data, offset)

        match = re.match(r'^bytes(\d+)$', type_)
        if match:
            size = int(match.group(1))
            return self.decode_fixed_bytes(bytes_data, offset, size)

        match = re.match(r'^(u?int)(\d+)$', type_)
        if match:
            signed = match.group(1) == 'int'

            return self.decode_number(bytes_data, offset, signed)

        if type_ == 'tuple':
            return self.decode_tuple(bytes_data, offset, param)

        raise Exception('Unsupported type: ' + type_)

    @staticmethod
    def decode_address(bytes_data, offset):
        data = bytes_data[offset:offset+32]
        address_bytes = data[12:32]
        address = '0x' + address_bytes.hex()
        address = Address.get_checksum_address(address)

        return address, 32

    @staticmethod
    def decode_bool(bytes_data, offset):
        data = bytes_data[offset:offset+32]
        value = int.from_bytes(data, byteorder='big') != 0

        return value, 32

    @staticmethod
    def decode_number(bytes_data, offset, signed):
        data = bytes_data[offset:offset+32]
        value = int.from_bytes(data, byteorder='big', signed=signed)

        return value, 32

    @classmethod
    def decode_string(cls, bytes_data, offset):
        data_offset = cls.read_uint(bytes_data, offset)
        string_offset = data_offset
        length = cls.read_uint(bytes_data, string_offset)
        string_data = bytes_data[string_offset+32:string_offset+32+length]
        value = string_data.decode('utf-8')

        return value, 32

    def decode_dynamic_bytes(self, bytes_data, offset):
        data_offset = self.read_uint(bytes_data, offset)
        bytes_offset = data_offset
        length = self.read_uint(bytes_data, bytes_offset)
        bytes_data_value = bytes_data[bytes_offset+32:bytes_offset+32+length]
        value = '0x' + bytes_data_value.hex()

        return value, 32

    def decode_fixed_bytes(self, bytes_data, offset, size):
        data = bytes_data[offset:offset+32]
        value = '0x' + data[:size].hex()
        return value, 32

    def decode_array(self, bytes_data, offset, param, length):
        base_type = param['type']
        element_type = param.copy()
        element_type['type'] = base_type

        if length is None:
            data_offset = self.read_uint(bytes_data, offset)
            array_offset = data_offset
            array_length = self.read_uint(bytes_data, array_offset)
            cursor = array_offset + 32
        else:
            array_length = length
            cursor = offset

        values = []
        for _ in range(array_length):
            value, consumed = self.decode_parameter(bytes_data, cursor, element_type)
            cursor += consumed
            values.append(value)

        return values, 32

    def decode_tuple(self, bytes_data, offset, param):
        components = param['components']
        values = {}
        cursor = offset

        for component in components:
            value, consumed = self.decode_parameter(bytes_data, cursor, component)
            cursor += consumed
            name = component.get('name', '')
            values[name] = value

        return values, 32

    @staticmethod
    def read_uint(bytes_data, offset):
        data = bytes_data[offset:offset+32]

        return int.from_bytes(data, byteorder='big')
