from datetime import datetime

from crypto.configuration.network import get_network, set_custom_network, set_network
from crypto.networks.devnet import Devnet
from crypto.networks.mainnet import Mainnet
from crypto.networks.testnet import Testnet


def test_get_network():
    result = get_network()
    assert result['version'] == 30


def test_set_network():
    # test main net
    set_network(Mainnet)
    result = get_network()
    assert result['version'] == 23
    assert result['wif'] == 170
    # test test net
    set_network(Testnet)
    result = get_network()
    assert result['version'] == 23
    assert result['wif'] == 186
    set_network(Devnet)  # set back to devnet so other tests don't fail


def test_set_custom_network():
    epoch_time = datetime(2017, 1, 1, 13, 00, 00)
    set_custom_network(epoch_time, 11, 130)
    result = get_network()
    assert result['version'] == 11
    assert result['wif'] == 130
    assert result['epoch'] == epoch_time
    set_network(Devnet)  # set back to devnet so other tests don't fail
