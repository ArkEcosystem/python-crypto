import hashlib
from binascii import unhexlify


class TransactionHasher:
    @staticmethod
    def to_hash(transaction: dict, skip_signature: bool = False) -> bytes:
        # Process recipientAddress
        hex_address = transaction.get('recipientAddress', '').lstrip('0x')
        # Pad with leading zero if necessary
        if len(hex_address) % 2 != 0:
            hex_address = '0' + hex_address
        recipient_address = bytes.fromhex(hex_address.lower())

        # Build the fields array
        fields = [
            TransactionHasher.to_be_array(int(transaction['network'])),
            TransactionHasher.to_be_array(int(transaction['nonce'])),
            TransactionHasher.to_be_array(int(transaction['gasPrice'])),  # maxPriorityFeePerGas
            TransactionHasher.to_be_array(int(transaction['gasPrice'])),  # maxFeePerGas
            TransactionHasher.to_be_array(int(transaction['gasLimit'])),
            recipient_address,
            TransactionHasher.to_be_array(int(transaction['value'])),
            bytes.fromhex(transaction.get('data', '').lstrip('0x')) if transaction.get('data') else b'',
            [],  # Access list is unused
        ]

        if not skip_signature and 'signature' in transaction:
            signature_buffer = bytes.fromhex(transaction['signature'])
            r = signature_buffer[0:32]
            s = signature_buffer[32:64]
            v = signature_buffer[64]
            fields.extend([
                TransactionHasher.to_be_array(v),
                r,
                s,
            ])

        eip1559_prefix = b'\x02'  # Marker for Type 2 (EIP-1559) transaction

        encoded = TransactionHasher.encode_rlp(fields)
        hash_input = eip1559_prefix + encoded

        # Use SHA256 for hashing
        return hashlib.sha256(hash_input).digest()

    @staticmethod
    def to_be_array(value):
        if isinstance(value, int):
            if value == 0:
                return b''  # Empty bytes represent zero
            else:
                return value.to_bytes((value.bit_length() + 7) // 8, byteorder='big')
        elif isinstance(value, bytes):
            return value
        else:
            raise TypeError("Unsupported type for to_be_array")

    @staticmethod
    def encode_length(length):
        if length == 0:
            return b''
        result = []
        while length > 0:
            result.insert(0, length & 0xFF)
            length >>= 8
        return bytes(result)

    @staticmethod
    def encode_rlp(input_data):
        if isinstance(input_data, bytes):
            input_len = len(input_data)
            if input_len == 1 and input_data[0] <= 0x7f:
                return input_data
            elif input_len <= 55:
                return bytes([0x80 + input_len]) + input_data
            else:
                len_bytes = TransactionHasher.encode_length(input_len)
                return bytes([0xb7 + len(len_bytes)]) + len_bytes + input_data
        elif isinstance(input_data, list):
            output = b''.join([TransactionHasher.encode_rlp(item) for item in input_data])
            output_len = len(output)
            if output_len <= 55:
                return bytes([0xc0 + output_len]) + output
            else:
                len_bytes = TransactionHasher.encode_length(output_len)
                return bytes([0xf7 + len(len_bytes)]) + len_bytes + output
        elif isinstance(input_data, int):
            return TransactionHasher.encode_rlp(TransactionHasher.to_be_array(input_data))
        elif input_data is None:
            return TransactionHasher.encode_rlp(b'')
        else:
            # Handle other types by converting to bytes
            return TransactionHasher.encode_rlp(str(input_data).encode('utf-8'))
