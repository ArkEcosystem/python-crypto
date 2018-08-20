from crypto.identity.private_key import PrivateKey


def test_private_key_from_passphrase(identity):
    private_key = PrivateKey.from_passphrase(identity['passphrase'])
    assert private_key.to_hex() == identity['data']['private_key']


def test_private_key_from_hex(identity):
    private_key = PrivateKey.from_hex(identity['data']['private_key'])
    assert private_key.to_hex() == identity['data']['private_key']
