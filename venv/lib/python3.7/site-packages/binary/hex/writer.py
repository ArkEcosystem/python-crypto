from binascii import unhexlify
from struct import pack


def write_low(data):
    """Write a hex string with low nibble first

    Args:
        data (int)

    Returns:
        bytes: bytes object containing data
    """
    return pack('<B', data)


def write_high(data):
    """Write a hex string with high nibble first

    Args:
        data (int)

    Returns:
        bytes: bytes object containing data
    """
    return unhexlify(data)
