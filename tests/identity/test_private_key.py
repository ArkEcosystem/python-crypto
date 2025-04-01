from crypto.identity.private_key import PrivateKey

def test_private_key_from_passphrase(identity):
    private_key = PrivateKey.from_passphrase(identity['passphrase'])
    assert isinstance(private_key, PrivateKey)
    assert private_key.to_hex() == identity['data']['private_key']


def test_private_key_from_hex(identity):
    private_key = PrivateKey.from_hex(identity['data']['private_key'])
    assert isinstance(private_key, PrivateKey)
    assert private_key.to_hex() == identity['data']['private_key']

def test_sign_compact(sign_compact):
    private_key = PrivateKey.from_passphrase(sign_compact['passphrase'])

    message = bytes.fromhex(sign_compact['data']['message'])
    signature = private_key.sign(message)

    assert signature[0] == sign_compact['data']['v']
    assert signature[1:33] == bytes.fromhex(sign_compact['data']['r'])
    assert signature[33:] == bytes.fromhex(sign_compact['data']['s'])
    assert signature.hex() == sign_compact['data']['serialized']
