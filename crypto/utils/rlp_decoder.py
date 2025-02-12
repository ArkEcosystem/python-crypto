import re
from typing import TypedDict

class DecodedType(TypedDict):
    consumed: int
    result: str | list

class RlpDecoder:
    @classmethod
    def decode(cls, data: str) -> str | list:
        bytes_data = cls.get_bytes(data, 'data')
        decoded = cls._decode(bytes_data, 0)

        if decoded['consumed'] != len(bytes_data):
            raise ValueError('unexpected junk after RLP payload')

        return decoded['result']

    @staticmethod
    def get_bytes(value: str, name: str = 'value') -> list[int]:
        if re.match(r'^0x(?:[0-9a-fA-F]{2})*$', value):
            hex_value = value[2:]
            length = len(hex_value) // 2
            bytes_data = [int(hex_value[i * 2:i * 2 + 2], 16) for i in range(length)]

            return bytes_data

        raise ValueError(f'Invalid BytesLike value for "{name}": {value}')

    @staticmethod
    def hexlify(data: list[int]) -> str:
        return '0x' + ''.join(f'{byte:02x}' for byte in data)

    @staticmethod
    def hexlify_byte(value: int) -> str:
        return f'0x{value & 0xff:02x}'

    @staticmethod
    def unarrayify_integer(data: list[int], offset: int, length: int) -> int:
        result = 0
        for i in range(length):
            result = (result << 8) + data[offset + i]

        return result

    @classmethod
    def _decode_children(cls, data: list[int], offset: int, child_offset: int, length: int) -> DecodedType:
        result = []
        end = offset + 1 + length

        while child_offset < end:
            decoded = cls._decode(data, child_offset)
            result.append(decoded['result'])
            child_offset += decoded['consumed']

            if child_offset > end:
                raise ValueError('child data too short or malformed')

        return {
            'consumed': 1 + length,
            'result': result,
        }

    @classmethod
    def _decode(cls, data: list[int], offset: int) -> DecodedType:
        cls.check_offset(offset, data)

        prefix = data[offset]

        if prefix >= 0xf8:
            length_length = prefix - 0xf7
            cls.check_offset(offset + length_length, data)

            length = cls.unarrayify_integer(data, offset + 1, length_length)
            cls.check_offset(offset + 1 + length_length + length - 1, data)

            return cls._decode_children(data, offset, offset + 1 + length_length, length_length + length)

        elif prefix >= 0xc0:
            length = prefix - 0xc0
            if length > 0:
                cls.check_offset(offset + 1 + length - 1, data)

            return cls._decode_children(data, offset, offset + 1, length)

        elif prefix >= 0xb8:
            length_length = prefix - 0xb7
            cls.check_offset(offset + length_length, data)

            length = cls.unarrayify_integer(data, offset + 1, length_length)
            if length > 0:
                cls.check_offset(offset + 1 + length_length + length - 1, data)
            slice_data = data[offset + 1 + length_length:offset + 1 + length_length + length]

            return {
                'consumed': 1 + length_length + length,
                'result': cls.hexlify(slice_data),
            }

        elif prefix >= 0x80:
            length = prefix - 0x80
            if length > 0:
                cls.check_offset(offset + 1 + length - 1, data)
            slice_data = data[offset + 1:offset + 1 + length]

            return {
                'consumed': 1 + length,
                'result': cls.hexlify(slice_data),
            }

        return {
            'consumed': 1,
            'result': cls.hexlify_byte(prefix),
        }

    @staticmethod
    def check_offset(offset: int, data: list[int]) -> None:
        if offset > len(data):
            raise ValueError('data short segment or out of range')
