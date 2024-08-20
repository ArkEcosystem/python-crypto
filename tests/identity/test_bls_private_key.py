from crypto.identity.bls_public_key import BLSPrivateKey


def test_private_key_from_passphrase(validator):
    private_key = BLSPrivateKey.from_passphrase(validator['passphrase']).to_hex()

    assert private_key == validator['bls_private_key']


def test_many_private_keys_from_passphrase(bls_keys):
    for bls_private_key in bls_keys:
        private_key = BLSPrivateKey.from_passphrase(bls_private_key['passphrase']).to_hex()

        assert private_key == bls_private_key['bls_private_key']
