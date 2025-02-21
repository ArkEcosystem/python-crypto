import binascii
from crypto.utils.abi_decoder import AbiDecoder

class ArgumentDecoder:
    def __init__(self, hex_string: str):
        try:
            self.bytes = binascii.unhexlify(hex_string)
        except binascii.Error:
            self.bytes = b''

    def decode_string(self) -> str:
        value, _ = AbiDecoder.decode_string(self.bytes, 0)

        return value

    def decode_address(self) -> str:
        value, _ = AbiDecoder.decode_address(self.bytes, 0)

        return value

    def decode_unsigned_int(self) -> int:
        value, _ = AbiDecoder.decode_number(self.bytes, 0, False)

        return value

    def decode_signed_int(self) -> int:
        value, _ = AbiDecoder.decode_number(self.bytes, 0, True)

        return value

    def decode_bool(self) -> bool:
        value, _ = AbiDecoder.decode_bool(self.bytes, 0)
        return value
