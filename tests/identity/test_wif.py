from crypto.identity.wif import wif_from_passphrase


def test_wif_from_passphrase(identity):
    result = wif_from_passphrase(identity['passphrase'])
    assert result == identity['data']['wif']
