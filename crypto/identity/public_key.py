from binascii import hexlify, unhexlify

from coincurve import PublicKey as PubKey

from crypto.identity.private_key import PrivateKey

class PublicKey(object):
    def __init__(self, public_key: str):
        self.public_key = PubKey(unhexlify(public_key.encode()))

    def to_hex(self) -> str:
        return hexlify(self.public_key.format()).decode()

    @classmethod
    def from_passphrase(cls, passphrase: str) -> str:
        private_key = PrivateKey.from_passphrase(passphrase)

        return private_key.public_key

    @classmethod
    def from_hex(cls, public_key):
        return cls(public_key)
