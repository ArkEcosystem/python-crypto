from datetime import datetime, timezone

from crypto.configuration.network import Network


def get_time() -> int:
    """Get the time difference between now and network start.

    Returns:
        int: difference in seconds
    """
    now = datetime.now(timezone.utc)

    seconds = int((now - get_epoch()).total_seconds())

    return seconds


def get_epoch():
    epoch_str = Network.get_network().epoch()
    if epoch_str.endswith("Z"):
        epoch_str = epoch_str[:-1] + "+00:00"

    return datetime.fromisoformat(epoch_str)
