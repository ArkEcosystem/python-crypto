from coincurve import PublicKey as PubKey

from crypto.identity.private_key import PrivateKey

class PublicKey(object):
    public_key: str

    def __init__(self, public_key: str):
        self.public_key = public_key

    @classmethod
    def from_passphrase(cls, passphrase: str) -> 'PublicKey':
        private_key = PrivateKey.from_passphrase(passphrase)

        return cls(private_key.public_key)

    @classmethod
    def from_hex(cls, public_key) -> 'PublicKey':
        return cls(public_key)

    @classmethod
    def recover(cls, message: bytes, signature: bytes) -> 'PublicKey':
        recovered_public_key = PubKey.from_signature_and_message(signature, message, hasher=None)

        return cls(recovered_public_key.format().hex())
