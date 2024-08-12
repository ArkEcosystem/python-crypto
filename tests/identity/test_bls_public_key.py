from crypto.identity.bls_public_key import BLSPublicKey


def test_public_key_from_passphrase(validator):
    public_key = BLSPublicKey.from_passphrase_attempt_1(validator['passphrase'])

    # assert public_key == validator['bls_public_key']
    print('attempt_1', public_key, validator['bls_public_key'])



    public_key = BLSPublicKey.from_passphrase_attempt_2(validator['passphrase'])

    # assert public_key == validator['bls_public_key']
    print('attempt_2', public_key, validator['bls_public_key'])



    public_key = BLSPublicKey.from_passphrase_attempt_3(validator['passphrase'])

    # assert public_key == validator['bls_public_key']
    print('attempt_3', public_key, validator['bls_public_key'])



    public_key = BLSPublicKey.from_passphrase_attempt_4(validator['passphrase'])

    # assert public_key == validator['bls_public_key']
    print('attempt_4', public_key, validator['bls_public_key'])



    public_key = BLSPublicKey.from_passphrase_attempt_5(validator['passphrase'])

    # assert public_key == validator['bls_public_key']
    print('attempt_5', public_key, validator['bls_public_key'])



    assert True == False


# def test_public_key_from_hex(validator):
#     public_key = BLSPublicKey.from_hex(validator['bls_public_key'])
#     assert isinstance(public_key, BLSPublicKey)
#     assert public_key.to_hex() == validator['bls_public_key']


