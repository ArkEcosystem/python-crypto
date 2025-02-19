from binascii import unhexlify
import hashlib

from Cryptodome.Hash import keccak
from crypto.enums.constants import Constants
from crypto.utils.rlp_encoder import RlpEncoder

class TransactionUtils:
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

        if not skip_signature and 'v' in transaction and 'r' in transaction and 's' in transaction:
            fields.append(cls.to_be_array(int(transaction['v']) - Constants.ETHEREUM_RECOVERY_ID_OFFSET.value))
            fields.append(bytes.fromhex(transaction['r']))
            fields.append(bytes.fromhex(transaction['s']))

        encoded = RlpEncoder.encode(fields)

        hash_input = Constants.EIP_1559_PREFIX.value + encoded

        return hash_input.encode()

    @classmethod
    def to_hash(cls, transaction: dict, skip_signature: bool = False) -> str:
        return keccak.new(data=unhexlify(cls.to_buffer(transaction, skip_signature)), digest_bits=256).hexdigest()

    @classmethod
    def get_id(cls, transaction: dict) -> str:
        return cls.to_hash(transaction)

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
