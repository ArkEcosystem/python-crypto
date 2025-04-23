from datetime import datetime, timezone

from crypto.configuration.network import Network

class Slot:
    @staticmethod
    def time() -> int:
        """Get the time difference between now and network start.

        Returns:
            int: difference in seconds
        """
        now = datetime.now(timezone.utc)

        return int(now.timestamp() - Slot.epoch())

    @staticmethod
    def epoch() -> int:
        epoch_str = Network.get_network().epoch()
        if epoch_str.endswith("Z"):
            epoch_str = epoch_str[:-1] + "+00:00"

        return int(datetime.fromisoformat(epoch_str).timestamp())
