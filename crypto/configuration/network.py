from datetime import datetime
from typing import Type, TypedDict, Union
from crypto.networks.mainnet import Mainnet
from crypto.networks.testnet import Testnet

class NetworkType(TypedDict):
    epoch: datetime
    version: int
    wif: int

network: NetworkType = {
    'epoch': Testnet.epoch,
    'version': Testnet.version,
    'wif': Testnet.wif,
}

def set_network(network_object: Union[Type[Mainnet], Type[Testnet]]) -> None:
    """Set what network you want to use in the crypto library

    Args:
        network_object: Testnet, Devnet, Mainnet
    """
    global network

    network = {
        'epoch': network_object.epoch,
        'version': network_object.version,
        'wif': network_object.wif,
    }

def get_network() -> NetworkType:
    """Get settings for a selected network, default network is devnet

    Returns:
        dict: network settings (default network is devnet)
    """
    return network

def set_custom_network(epoch: datetime, version: int, wif: int) -> None:
    """Set custom network

    Args:
        epoch (datetime): chains epoch time
        version (int): chains version
        wif (int): chains wif
    """
    global network

    network = {
        'epoch': epoch,
        'version': version,
        'wif': wif,
    }
