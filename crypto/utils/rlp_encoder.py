from binascii import hexlify, unhexlify


class RlpEncoder:
    @classmethod
    def encode(cls, obj) -> str:
        encoded = cls._encode(obj)
        hex_str = ''
        nibbles = '0123456789abcdef'

        for byte in encoded:
            hex_str += nibbles[byte >> 4]
            hex_str += nibbles[byte & 0x0f]

        return hex_str

    @classmethod
    def _encode(cls, obj) -> list:
        if isinstance(obj, list):
            payload = []
            for child in obj:
                payload.extend(cls._encode(child))

            payload_length = len(payload)
            if payload_length <= 55:
                payload.insert(0, 0xc0 + payload_length)

                return payload

            length = cls.arrayify_integer(payload_length)
            length.insert(0, 0xf7 + (len(length)))

            return length + payload

        data = cls.get_bytes(obj)
        data_length = len(data)
        if data_length == 1 and data[0] <= 0x7f:
            return data

        if data_length <= 55:
            data.insert(0, 0x80 + data_length)

            return data

        length = cls.arrayify_integer(len(data))
        length.insert(0, 0xb7 + len(length))

        return length + data

    @staticmethod
    def arrayify_integer(value) -> list:
        result = []
        while value > 0:
            result.insert(0, value & 0xff)
            value >>= 8

        return result

    @staticmethod
    def get_bytes(value) -> list:
        if isinstance(value, str) or isinstance(value, bytes):
            if isinstance(value, str):
                value = value.encode()

            if value.startswith(b'0x'):
                hex_str = value[2:]
                if hex_str == '':
                    return []

                if len(hex_str) % 2 != 0:
                    hex_str = b'0' + hex_str

                return [int(hex_str[i:i+2], 16) for i in range(0, len(hex_str), 2)]

            return [char for char in value]

        if isinstance(value, int):
            if value == 0:
                return []

            result = []
            while value > 0:
                result.insert(0, value & 0xff)
                value >>= 8

            return result

        if isinstance(value, list):
            return [v & 0xff for v in value]

        raise ValueError('invalid type', type(value))
