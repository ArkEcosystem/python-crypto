import os
import sys
from btclib.mnemonic import bip39

os.environ['VIRTUAL_ENV']

sys.path.append(os.path.join(os.environ['VIRTUAL_ENV'], 'src', 'blspy', 'python-impl'))

from schemes import BasicSchemeMPL # type: ignore


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

        sk = BasicSchemeMPL.key_gen(seed)

        return cls(bytes(BasicSchemeMPL.derive_child_sk(sk, 0)))
