from crypto.identity.legacy_address import LegacyAddress


def test_from_passphrase(legacy_identity):
    address = LegacyAddress.from_passphrase(legacy_identity['passphrase'], legacy_identity['pub_key_hash'])
    assert address == legacy_identity['data']['address']


def test_from_public_key(legacy_identity):
    address = LegacyAddress.from_public_key(legacy_identity['data']['public_key'], legacy_identity['pub_key_hash'])
    assert address == legacy_identity['data']['address']


def test_from_private_key(legacy_identity):
    address = LegacyAddress.from_private_key(legacy_identity['data']['private_key'], legacy_identity['pub_key_hash'])
    assert address == legacy_identity['data']['address']


def test_validate(legacy_identity):
    assert LegacyAddress.validate(legacy_identity['data']['address'], legacy_identity['pub_key_hash']) is True


def test_validate_incorrect_pub_key_hash(legacy_identity):
    assert LegacyAddress.validate(legacy_identity['data']['address'], 32) is False


def test_validate_invalid_address(legacy_identity):
    assert LegacyAddress.validate('D2WFnqYDRiFkSf4ezzWRt3jCsUp2sRmDMifwd', legacy_identity['pub_key_hash']) is False


def test_validate_decoding_error(legacy_identity):
    assert LegacyAddress.validate('invalid', legacy_identity['pub_key_hash']) is False
