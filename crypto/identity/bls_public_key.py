import sys
import os
from os.path import dirname

sys.path.append(os.path.join(dirname(dirname(__file__)), 'thirdparty/bls-signatures/python-impl'))

from schemes import PrivateKey

from crypto.identity.bls_private_key import BLSPrivateKey

class BLSPublicKey:
    def __init__(self, public_key: bytes):
        self.public_key = public_key

    def to_hex(self) -> str:
        return self.public_key.hex()

    @classmethod
    def from_passphrase(cls, passphrase: str):
        private_key = BLSPrivateKey.from_passphrase(passphrase)

        return cls(bytes(PrivateKey.from_bytes(private_key.private_key).get_g1()))
