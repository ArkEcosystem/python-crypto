from crypto.configuration.network import Network
from crypto.identity.wif import WIF
from crypto.networks.testnet import Testnet


def test_wif_from_passphrase(identity):
    Network.set_network(Testnet())

    result = WIF.from_passphrase(identity['passphrase'])
    assert result == identity['data']['wif']
