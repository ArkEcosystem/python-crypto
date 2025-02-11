from binascii import hexlify, unhexlify
import hashlib

from crypto.utils.rlp_encoder import RlpEncoder

class TransactionUtils:
    EIP1559_PREFIX = '02'

    @classmethod
    def to_buffer(cls, transaction: dict, skip_signature: bool = False) -> bytes:
        # Process recipientAddress
        hex_address = transaction.get('recipientAddress', '').lstrip('0x')

        # Pad with leading zero if necessary
        if len(hex_address) % 2 != 0:
            hex_address = '0' + hex_address

        recipient_address = bytes.fromhex(hex_address.lower())

        # Build the fields array
        fields = [
            cls.to_be_array(int(transaction['network'])),
            cls.to_be_array(int(transaction.get('nonce', 0))),
            cls.to_be_array(0),
            cls.to_be_array(int(transaction['gasPrice'])),
            cls.to_be_array(int(transaction['gasLimit'])),
            recipient_address,
            cls.to_be_array(int(transaction.get('value', 0))),
            bytes.fromhex(transaction.get('data', '').lstrip('0x')) if transaction.get('data') else b'',
            [],
        ]

        if not skip_signature and 'signature' in transaction:
            signature_buffer = bytes.fromhex(transaction['signature'])
            r = signature_buffer[0:32]
            s = signature_buffer[32:64]
            v = signature_buffer[64]
            fields.extend([
                cls.to_be_array(v),
                r,
                s,
            ])

        # print('FIELDS', fields, len(fields))
        # print('FIELDS', [f.hex() for f in fields])

        # FIELDS [b'1e', b'01', b'', b'05', b'5208', b'6f0182a0cc707b055322ccf6d4cb6a5aff1aeb22', b'05f5e100', b'']

        encoded = RlpEncoder.encode(fields)

        # print('ENCODED', encoded)
        # \xf8C\x821e\x8201\x80\x8205\x845208\xa86f0182a0cc707b055322ccf6d4cb6a5aff1aeb22\x8805f5e100\x80\xc0
        # print('ACTUAL  0xe31e018005825208946f0182a0cc707b055322ccf6d4cb6a5aff1aeb228405f5e10080c0')

        hash_input = cls.EIP1559_PREFIX + encoded

        print('HASH_INPUT', hash_input)
        print('EXPECTED   02e31e018005825208946f0182a0cc707b055322ccf6d4cb6a5aff1aeb228405f5e10080c0')
        print('MATCH', hash_input == '02e31e018005825208946f0182a0cc707b055322ccf6d4cb6a5aff1aeb228405f5e10080c0')

        # Use SHA256 for hashing
        return hash_input.encode()

    @classmethod
    def to_hash(cls, transaction: dict, skip_signature: bool = False) -> str:
        return hashlib.sha256(unhexlify(cls.to_buffer(transaction, skip_signature))).hexdigest()

    @staticmethod
    def to_be_array(value):
        if isinstance(value, int):
            if value == 0:
                return b''
            else:
                return value.to_bytes((value.bit_length() + 7) // 8, byteorder='big')

        if isinstance(value, bytes):
            return value

        raise TypeError("Unsupported type for to_be_array")
