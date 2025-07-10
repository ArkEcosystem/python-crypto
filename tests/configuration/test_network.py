from datetime import datetime

from crypto.configuration.network import Network
from crypto.networks.abstract_network import AbstractNetwork
from crypto.networks.testnet import Testnet
from crypto.networks.mainnet import Mainnet

class CustomNetwork(AbstractNetwork):
    def epoch(self):
        return "2024-01-01T13:00:00.000Z"

    def wif(self):
        return "82"

    def chain_id(self):
        return 20000

def test_get_network():
    result = Network.get_network()
    assert result.chain_id() == 11812

def test_set_network():
    # mainnet
    Network.set_network(Mainnet())
    result = Network.get_network()
    assert result.wif() == 'ba'
    assert result.chain_id() == 11811

    # testnet
    Network.set_network(Testnet())
    result = Network.get_network()
    assert result.wif() == 'ba'
    assert result.chain_id() == 11812

    Network.set_network(Testnet())  # set back to Testnet so other tests don't fail

def test_set_custom_network():
    Network.set_network(CustomNetwork())
    result = Network.get_network()
    assert result.wif() == '82'
    assert result.epoch() == "2024-01-01T13:00:00.000Z"
    assert result.chain_id() == 20000

    Network.set_network(Testnet())  # set back to Testnet so other tests don't fail
