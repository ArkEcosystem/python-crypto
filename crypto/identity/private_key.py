from binascii import hexlify
from hashlib import sha256

from btclib.to_prv_key import PrvKey, int_from_prv_key
from btclib.to_pub_key import pub_keyinfo_from_key
from btclib.ecc import bms

class PrivateKey(object):
    private_key: PrvKey
    private_key_raw: str

    def __init__(self, private_key: str):
        self.private_key_raw = private_key
        self.private_key = int_from_prv_key(private_key)
        self.public_key = hexlify(pub_keyinfo_from_key(self.private_key)[0]).decode()

    def sign(self, message: bytes) -> bytes:
        """Sign a message with this private key object

        Args:
            message (bytes): bytes data you want to sign

        Returns:
            bytes: signature of the signed message
        """
        signature = bms.sign(message, self.private_key)

        return signature.serialize()

    def sign_compact(self, message: bytes) -> bms.Sig:
        """Sign a message with this private key object

        Args:
            message (bytes): bytes data you want to sign

        Returns:
            bytes: signature of the signed message
        """
        return bms.sign(message, self.private_key)
        # wif, address = bms.gen_keys(self.private_key, compressed=True)

        # # print('WIF', wif)
        # # print('address', address)

        # return bms.sign(message, wif, address)

    def to_hex(self):
        """Returns a private key in hex format

        Returns:
            str: private key in hex format
        """
        return hexlify(self.private_key.to_bytes(32, 'big')).decode()

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
