from struct import pack


def write_bit8(data):
    """Write a signed 8 bit integer

    Args:
        data (int)

    Returns:
        bytes: bytes object containing value from data
    """
    return pack('b', data)[1]


def write_bit16(data):
    """Write a signed 16 bit integer

    Args:
        data (int)

    Returns:
        bytes: bytes object containing value from data
    """
    return pack('h', data)[1]


def write_bit32(data):
    """Write a signed 32 bit integer

    Args:
        data (int)

    Returns:
        bytes: bytes object containing value from data
    """
    return pack('l', data)[1]


def write_bit64(data):
    """Write a signed 64 bit integer

    Args:
        data (int)

    Returns:
        bytes: bytes object containing value from data
    """
    return pack('q', data)[1]
