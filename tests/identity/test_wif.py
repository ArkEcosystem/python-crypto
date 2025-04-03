from crypto.configuration.network import set_network
from crypto.identity.wif import WIF
from crypto.networks.testnet import Testnet


def test_wif_from_passphrase(identity):
    set_network(Testnet)

    result = WIF.from_passphrase(identity['passphrase'])
    assert result == identity['data']['wif']
