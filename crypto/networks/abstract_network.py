from abc import ABC, abstractmethod

class AbstractNetwork(ABC):
    @abstractmethod
    def chain_id(self) -> int:
        """Return the chain ID of the network."""

    @abstractmethod
    def epoch(self) -> str:
        """Return the epoch time of the network."""

    @abstractmethod
    def wif(self) -> str:
        """Return the WIF (Wallet Import Format) of the network."""
