from btclib.mnemonic import bip39

from crypto.utils import bls

class BLSPrivateKey(object):
    def __init__(self, private_key: bytes):
        self.private_key = private_key

    def to_hex(self):
        """Returns a private key in hex format

        Returns:
            str: private key in hex format
        """
        return self.private_key.hex()

    @classmethod
    def from_passphrase(cls, passphrase: str):
        """Create PrivateKey object from a given passphrase

        Args:
            passphrase (str):

        Returns:
            PrivateKey: Private key object
        """
        seed = bip39.seed_from_mnemonic(passphrase, '')

        master_key = bls.deriveMaster(seed)
        child_key_secret_key = bls.deriveChild(master_key, 0)

        return cls(child_key_secret_key)
