from datetime import datetime

from crypto.configuration.network import get_network

class Slot:
    @staticmethod
    def time():
        """Get the time difference between now and network start.

        Returns:
            int: difference in seconds
        """
        now = datetime.utcnow()
        network = get_network()
        seconds = int((now - network['epoch']).total_seconds())
        return seconds

    @staticmethod
    def epoch():
        network = get_network()
        return network['epoch']
