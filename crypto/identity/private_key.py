from binascii import hexlify
from hashlib import sha256

from coincurve import PrivateKey as PvtKey


class PrivateKey(object):

    def __init__(self, private_key):
        self.private_key = PvtKey.from_hex(private_key)
        self.public_key = hexlify(self.private_key.public_key.format()).decode()

    def sign(self, message):
        """Sign a message with this private key object

        Args:
            message (bytes): bytes data you want to sign

        Returns:
            str: signature of the signed message
        """
        signature = self.private_key.sign(message)
        return hexlify(signature).decode()

    def to_hex(self):
        """Returns a private key in hex format

        Returns:
            str: private key in hex format
        """
        return self.private_key.to_hex()

    @classmethod
    def from_passphrase(cls, passphrase):
        """Create PrivateKey object from a given passphrase

        Args:
            passphrase (str):

        Returns:
            PrivateKey: Private key object
        """
        private_key = sha256(passphrase.encode()).hexdigest()
        return cls(private_key)

    @classmethod
    def from_hex(cls, private_key):
        """Create PrivateKey object from a given hex private key

        Args:
            private_key (str):

        Returns:
            PrivateKey: Private key object
        """
        return cls(private_key)
