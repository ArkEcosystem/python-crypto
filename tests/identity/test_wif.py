from crypto.conf import use_network
from crypto.identity.wif import wif_from_passphrase


def test_wif_from_passphrase(identity):
    use_network('devnet')
    result = wif_from_passphrase(identity['passphrase'])
    assert result == identity['data']['wif']
