from datetime import datetime

from crypto.configuration.network import get_network, set_custom_network, set_network
from crypto.networks.testnet import Testnet
from crypto.networks.mainnet import Mainnet
from crypto.networks.testnet import Testnet


def test_get_network():
    result = get_network()
    assert result['version'] == 30


def test_set_network():
    # mainnet
    set_network(Mainnet)
    result = get_network()
    assert result['version'] == 30
    assert result['wif'] == 186

    # testnet
    set_network(Testnet)
    result = get_network()
    assert result['version'] == 30
    assert result['wif'] == 186

    set_network(Testnet)  # set back to Testnet so other tests don't fail


def test_set_custom_network():
    epoch_time = datetime(2017, 1, 1, 13, 00, 00)
    set_custom_network(epoch_time, 11, 130)
    result = get_network()
    assert result['version'] == 11
    assert result['wif'] == 130
    assert result['epoch'] == epoch_time

    set_network(Testnet)  # set back to Testnet so other tests don't fail
