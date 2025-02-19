from crypto.configuration.network import set_network
from crypto.identity.wif import wif_from_passphrase
from crypto.networks.testnet import Testnet


def test_wif_from_passphrase(identity):
    set_network(Testnet)

    result = wif_from_passphrase(identity['passphrase'])
    assert result == identity['data']['wif']
