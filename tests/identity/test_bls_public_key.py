from crypto.identity.bls_public_key import BLSPublicKey


def test_public_key_from_passphrase(validator):
    public_key = BLSPublicKey.from_passphrase(validator['passphrase'])
    assert public_key == validator['bls_public_key']


# def test_public_key_from_hex(validator):
#     public_key = BLSPublicKey.from_hex(validator['bls_public_key'])
#     assert isinstance(public_key, BLSPublicKey)
#     assert public_key.to_hex() == validator['bls_public_key']


