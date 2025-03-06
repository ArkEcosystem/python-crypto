from datetime import datetime
from typing import Type, TypedDict, Union
from crypto.networks.mainnet import Mainnet
from crypto.networks.testnet import Testnet

class NetworkType(TypedDict):
    epoch: datetime
    wif: int
    chain_id: int

network: NetworkType = {
    'epoch': Testnet.epoch,
    'wif': Testnet.wif,
    'chain_id': Testnet.chain_id,
}

def set_network(network_object: Union[Type[Mainnet], Type[Testnet]]) -> None:
    """Set what network you want to use in the crypto library

    Args:
        network_object: Testnet, Devnet, Mainnet
    """
    global network

    network = {
        'epoch': network_object.epoch,
        'wif': network_object.wif,
        'chain_id': network_object.chain_id,
    }

def get_network() -> NetworkType:
    """Get settings for a selected network, default network is devnet

    Returns:
        dict: network settings (default network is devnet)
    """
    return network

def set_custom_network(epoch: datetime, wif: int, chain_id: int) -> None:
    """Set custom network

    Args:
        epoch (datetime): chains epoch time
        wif (int): chains wif
        chain_id (int): chain id
    """
    global network

    network = {
        'epoch': epoch,
        'wif': wif,
        'chain_id': chain_id
    }
