from crypto.networks.abstract_network import AbstractNetwork
from crypto.networks.testnet import Testnet

class Network:
    _network: AbstractNetwork

    @classmethod
    def set_network(cls, network: AbstractNetwork) -> None:
        """Set what network you want to use in the crypto library

        Args:
            network_object: Testnet, Devnet, Mainnet
        """

        cls._network = network

    @classmethod
    def get_network(cls) -> AbstractNetwork:
        """Get settings for a selected network

        Returns:
            AbstractNetwork: network settings (default network is testnet)
        """
        return cls._network

Network.set_network(Testnet())
