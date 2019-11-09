from struct import pack


def write_bit8(data):
    return pack('B', data)


def write_bit16(data, endianness=False):
    """Write an unsigned 16 bit integer

    Args:
        data (int)

    Returns:
        bytes: bytes object containing value from data
    """

    if endianness is True:
        value = pack('>H', data)  # big-endian
    elif endianness is False:
        value = pack('<H', data)  # little-endian
    elif endianness is None:
        value = pack('H', data)  # machine byte order
    else:
        raise Exception('Invalid value "{}" for endianness given'.format(endianness))
    return value


def write_bit32(data, endianness=False):
    """Write an unsigned 32 bit integer

    Args:
        data (int)

    Returns:
        bytes: bytes object containing value from data
    """
    if endianness is True:
        value = pack('>L', data)  # big-endian
    elif endianness is False:
        value = pack('<L', data)  # little-endian
    elif endianness is None:
        value = pack('L', data)  # machine byte order
    else:
        raise Exception('Invalid value "{}" for endianness given'.format(endianness))
    return value


def write_bit64(data, endianness=False):
    """Write an unsigned 64 bit integer

    Args:
        data (int)

    Returns:
        bytes: bytes object containing value from data
    """
    if endianness is True:
        value = pack('>Q', data)  # big-endian
    elif endianness is False:
        value = pack('<Q', data)  # little-endian
    elif endianness is None:
        value = pack('Q', data)  # machine byte order
    else:
        raise Exception('Invalid value "{}" for endianness given'.format(endianness))
    return value
