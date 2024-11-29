# crypto/utils/abi_encoder.py

from crypto.utils.abi_base import AbiBase
import binascii


class AbiEncoder(AbiBase):
    def encode_function_call(self, function_name, args=[]):
        parameters = {
            'abi': self.abi,
            'functionName': function_name,
            'args': args,
        }
        return self.encode_function_data(parameters)

    def encode_function_data(self, parameters):
        args = parameters.get('args', [])

        if (len(parameters['abi']) == 1 and
                'functionName' in parameters and
                parameters['functionName'].startswith('0x')):
            abi_item = parameters['abi'][0]
            function_name = parameters['functionName']
        else:
            abi_item, function_name = self.prepare_encode_function_data(parameters)

        signature = function_name

        if abi_item.get('inputs'):
            data = self.encode_abi_parameters(abi_item['inputs'], args)
        else:
            data = None

        return self.concat_hex([signature, data or '0x'])

    def prepare_encode_function_data(self, params):
        abi = params['abi']
        function_name = params.get('functionName')

        if not function_name:
            functions = [item for item in abi if item['type'] == 'function']
            if len(functions) == 1:
                abi_item = functions[0]
                function_name = abi_item['name']
            else:
                raise Exception('Function name is not provided and ABI has multiple functions')
        else:
            abi_item = self.get_abi_item(abi, function_name, params.get('args', []))
            if not abi_item:
                raise Exception('Function not found in ABI: ' + function_name)

        signature = self.to_function_selector(abi_item)
        return abi_item, signature

    def get_abi_item(self, abi, name, args):
        matching_items = [item for item in abi if item['type'] == 'function' and item['name'] == name]
        if not matching_items:
            raise Exception(f"Function not found in ABI: {name}")

        for item in matching_items:
            inputs = item.get('inputs', [])
            if len(inputs) == len(args):
                return item

        raise Exception(f"Function with matching arguments not found in ABI: {name}")

    def encode_abi_parameters(self, params, values):
        if len(params) != len(values):
            raise Exception('Length of parameters and values do not match')
        prepared_params = self.prepare_params(params, values)
        data = self.encode_params(prepared_params)
        return data if data != '' else '0x'

    def prepare_params(self, params, values):
        prepared_params = []
        for index, param in enumerate(params):
            prepared_param = self.prepare_param(param, values[index])
            prepared_params.append(prepared_param)
        return prepared_params

    def prepare_param(self, param, value):
        array_components = self.get_array_components(param['type'])
        if array_components:
            length, type_ = array_components
            return self.encode_array(value, length, {'name': param['name'], 'type': type_})
        if param['type'] == 'tuple':
            return self.encode_tuple(value, param)
        if param['type'] == 'address':
            return self.encode_address(value)
        if param['type'] == 'bool':
            return self.encode_bool(value)
        if param['type'].startswith('uint') or param['type'].startswith('int'):
            signed = param['type'].startswith('int')
            return self.encode_number(value, signed)
        if param['type'].startswith('bytes'):
            return self.encode_bytes(value, param)
        if param['type'] == 'string':
            return self.encode_string(value)
        raise Exception('Invalid ABI type: ' + param['type'])

    def encode_array(self, value, length, param):
        dynamic = length is None

        if not isinstance(value, list):
            raise Exception('Invalid array value')
        if not dynamic and len(value) != length:
            raise Exception('Array length mismatch')

        dynamic_child = False
        prepared_params = []
        for v in value:
            prepared_param = self.prepare_param(param, v)
            if prepared_param['dynamic']:
                dynamic_child = True
            prepared_params.append(prepared_param)

        if dynamic or dynamic_child:
            data = self.encode_params(prepared_params)
            if dynamic:
                length_hex = '{:064x}'.format(len(prepared_params))
                return {
                    'dynamic': True,
                    'encoded': '0x' + length_hex + data[2:],
                }
            if dynamic_child:
                return {
                    'dynamic': True,
                    'encoded': data,
                }
        encoded = ''.join([p['encoded'][2:] for p in prepared_params])
        return {
            'dynamic': False,
            'encoded': '0x' + encoded,
        }

    def encode_params(self, prepared_params):
        static_size = 0
        for param in prepared_params:
            if param['dynamic']:
                static_size += 32
            else:
                static_size += (len(param['encoded']) - 2) // 2

        static_params = []
        dynamic_params = []
        dynamic_size = 0
        for param in prepared_params:
            if param['dynamic']:
                offset = '{:064x}'.format(static_size + dynamic_size)
                static_params.append(offset)
                dynamic_params.append(param['encoded'][2:])
                dynamic_size += (len(param['encoded']) - 2) // 2
            else:
                static_params.append(param['encoded'][2:])

        encoded = '0x' + ''.join(static_params) + ''.join(dynamic_params)
        return encoded

    def encode_address(self, value):
        if not self.is_valid_address(value):
            raise Exception('Invalid address: ' + value)
        value = self.strip_hex_prefix(value.lower())
        return {
            'dynamic': False,
            'encoded': '0x' + value.zfill(64),
        }

    def encode_bool(self, value):
        encoded = '1' if value else '0'
        encoded = encoded.zfill(64)
        return {
            'dynamic': False,
            'encoded': '0x' + encoded,
        }

    def encode_number(self, value, signed):
        if not isinstance(value, int) and not isinstance(value, str):
            raise Exception('Invalid number value')
        if isinstance(value, str):
            value = int(value)
        if signed:
            if value < 0:
                value = (1 << 256) + value
        else:
            if value < 0:
                raise Exception('Negative value provided for unsigned integer type')
        hex_value = '{:x}'.format(value)
        encoded = hex_value.zfill(64)
        return {
            'dynamic': False,
            'encoded': '0x' + encoded,
        }

    def encode_bytes(self, value, param):
        if isinstance(value, str) and value.startswith('0x'):
            value = value[2:]
        bytes_size = len(value) // 2
        param_size_str = param['type'][5:]
        if param_size_str == '':
            length_hex = '{:064x}'.format(bytes_size)
            value_padded = value
            padding = (32 - (bytes_size % 32)) % 32
            if padding > 0:
                value_padded += '00' * padding
            return {
                'dynamic': True,
                'encoded': '0x' + length_hex + value_padded,
            }
        param_size = int(param_size_str)
        if bytes_size != param_size:
            raise Exception(f"Bytes size mismatch: expected {param_size}, got {bytes_size}")
        value_padded = value.ljust(64, '0')
        return {
            'dynamic': False,
            'encoded': '0x' + value_padded,
        }

    def encode_string(self, value):
        hex_value = binascii.hexlify(value.encode('utf-8')).decode()
        length_hex = '{:064x}'.format(len(value))
        value_padded = hex_value
        padding = (32 - (len(value) % 32)) % 32
        if padding > 0:
            value_padded += '00' * padding
        return {
            'dynamic': True,
            'encoded': '0x' + length_hex + value_padded,
        }

    def encode_tuple(self, value, param):
        dynamic = False
        prepared_params = []
        for index, component in enumerate(param['components']):
            key = index if isinstance(value, list) else component.get('name')
            if key not in value:
                raise Exception('Tuple value missing component: ' + component.get('name', ''))
            prepared_param = self.prepare_param(component, value[key])
            if prepared_param['dynamic']:
                dynamic = True
            prepared_params.append(prepared_param)
        if dynamic:
            encoded = self.encode_params(prepared_params)
            return {
                'dynamic': True,
                'encoded': encoded,
            }
        encoded = '0x' + ''.join([p['encoded'][2:] for p in prepared_params])
        return {
            'dynamic': False,
            'encoded': encoded,
        }

    def concat_hex(self, hexes):
        result = '0x'
        for hex_str in hexes:
            if not hex_str or hex_str == '0x':
                continue
            result += self.strip_hex_prefix(hex_str)
        return result
