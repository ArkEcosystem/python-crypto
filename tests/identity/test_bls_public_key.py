from crypto.identity.bls_public_key import BLSPublicKey


def test_public_key_from_passphrase(validator):
    public_key = BLSPublicKey.from_passphrase(validator['passphrase']).to_hex()

    assert public_key == validator['bls_public_key']


def test_many_public_keys_from_passphrase(bls_keys):
    for bls_public_key in bls_keys:
        private_key = BLSPublicKey.from_passphrase(bls_public_key['passphrase']).to_hex()

        assert private_key == bls_public_key['bls_public_key']
