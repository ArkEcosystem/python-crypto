from binascii import hexlify
from hashlib import sha256
from coincurve import PrivateKey as PvtKey
from Cryptodome.Hash import keccak
from base58 import b58decode

from crypto.configuration.network import get_network
from crypto.enums.constants import Constants

def keccak256(data: bytes) -> bytes:
    """Keccak256 hash function"""

    return bytes.fromhex(keccak.new(data=data, digest_bits=256).hexdigest())

class PrivateKey(object):
    def __init__(self, private_key: str):
        self.private_key = PvtKey.from_hex(private_key)
        self.public_key = hexlify(self.private_key.public_key.format()).decode()

    def sign(self, message: bytes) -> bytes:
        """Sign a message with this private key object

        Args:
            message (bytes): bytes data you want to sign

        Returns:
            bytes: signature of the signed message
        """
        signature = self.private_key.sign(message)

        return hexlify(signature)

    def sign_compact(self, message: bytes) -> bytes:
        """Sign a message with this private key object

        Args:
            message (bytes): bytes data you want to sign

        Returns:
            bytes: signature of the signed message
        """
        der = self.private_key.sign_recoverable(message, hasher=keccak256)

        return bytes([der[64] + Constants.ETHEREUM_RECOVERY_ID_OFFSET.value]) + der[0:64]

    def to_hex(self):
        """Returns a private key in hex format

        Returns:
            str: private key in hex format
        """
        return self.private_key.to_hex()

    @classmethod
    def from_passphrase(cls, passphrase: str):
        """Create PrivateKey object from a given passphrase

        Args:
            passphrase (str):

        Returns:
            PrivateKey: Private key object
        """
        private_key = sha256(passphrase.encode()).hexdigest()

        return cls(private_key)

    @classmethod
    def from_hex(cls, private_key: str):
        """Create PrivateKey object from a given hex private key

        Args:
            private_key (str):

        Returns:
            PrivateKey: Private key object
        """
        return cls(private_key)

    @classmethod
    def from_wif(cls, wif: str):
        """Create PrivateKey object from a given wif

        Args:
            wif (str):

        Returns:
            PrivateKey: Private key object
        """

        wif = b58decode(wif).hex()

        version = wif[0:2]
        if version != get_network()['wif']:
            raise ValueError(f"Invalid WIF version: {version}")

        private_key = wif[2:66]

        return cls(private_key)
