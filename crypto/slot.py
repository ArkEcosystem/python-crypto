from datetime import datetime

from crypto.conf import get_network


def get_time():
    """Get the time difference between now and network start.

    Returns:
        int: difference in seconds
    """
    now = datetime.utcnow()
    network = get_network()
    diff = (now - network['epoch']).seconds
    return diff
