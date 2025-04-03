from binascii import hexlify
from crypto.identity.public_key import PublicKey


def test_public_key_from_passphrase(identity):
    public_key = PublicKey.from_passphrase(identity['passphrase'])
    assert public_key == identity['data']['public_key']


def test_public_key_from_hex(identity):
    public_key = PublicKey.from_hex(identity['data']['public_key'])
    assert isinstance(public_key, PublicKey)

    public_key_hex = hexlify(public_key.public_key.format()).decode()

    assert public_key_hex == identity['data']['public_key']
