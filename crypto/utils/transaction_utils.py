from binascii import unhexlify
import re

from Cryptodome.Hash import keccak
from crypto.configuration.network import Network
from crypto.utils.rlp_encoder import RlpEncoder

class TransactionUtils:
    @classmethod
    def to_buffer(cls, transaction: dict, skip_signature: bool = False) -> bytes:
        hex_address = cls.parse_hex_from_str(transaction.get('to', ''))

        # Pad with leading zero if necessary
        if len(hex_address) % 2 != 0:
            hex_address = '0' + hex_address

        to = bytes.fromhex(hex_address.lower())

        # Build the fields array
        fields = [
            cls.to_be_array(int(transaction.get('nonce', 0))),
            cls.to_be_array(int(transaction['gasPrice'])),
            cls.to_be_array(int(transaction['gasLimit'])),
            to,
            cls.to_be_array(int(transaction.get('value', 0))),
            bytes.fromhex(cls.parse_hex_from_str(transaction.get('data', ''))) if transaction.get('data') else b'',
        ]

        if not skip_signature and 'v' in transaction and transaction['v'] is not None and 'r' in transaction and 's' in transaction:
            fields.append(cls.to_be_array(int(transaction['v']) + (Network.get_network().chain_id() * 2 + 35)))
            fields.append(bytes.fromhex(transaction['r']))
            fields.append(bytes.fromhex(transaction['s']))

            if 'legacySecondSignature' in transaction and transaction['legacySecondSignature']:
                fields.append(bytes.fromhex(transaction['legacySecondSignature']))
        else:
            # Push chainId + 0s for r and s
            fields.append(cls.to_be_array(Network.get_network().chain_id()))
            fields.append(cls.to_be_array(0))
            fields.append(cls.to_be_array(0))

        encoded = RlpEncoder.encode(fields)

        return encoded.encode()

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

    @staticmethod
    def parse_hex_from_str(value: str) -> str:
        return re.sub(r'^0x', '', value)
