from struct import unpack_from


def read_bit8(data, offset=0):
    """Read an unsigned 8 bit integer

    Args:
        data (bytes)

    Returns:
        int
    """
    return unpack_from('B', data, offset)[0]


def read_bit16(data, offset=0, endianness=False):
    """Read an unsigned 16 bit integer

    Args:
        data (bytes)

    Returns:
        int
    """
    if endianness is True:
        value = unpack_from('>H', data, offset)[0]  # big-endian
    elif endianness is False:
        value = unpack_from('<H', data, offset)[0]  # little-endian
    elif endianness is None:
        value = unpack_from('=H', data, offset)[0]  # machine byte order
    else:
        raise Exception('Invalid value "{}" for endianness given'.format(endianness))
    return value


def read_bit32(data, offset=0, endianness=False):
    """Read an unsigned 32 bit integer

    Args:
        data (bytes)

    Returns:
        int
    """
    if endianness is True:
        value = unpack_from('>L', data, offset)[0]  # big-endian
    elif endianness is False:
        value = unpack_from('<L', data, offset)[0]  # little-endian
    elif endianness is None:
        value = unpack_from('L', data, offset)[0]  # machine byte order
    else:
        raise Exception('Invalid value "{}" for endianness given'.format(endianness))
    return value


def read_bit64(data, offset=0, endianness=False):
    """Read an unsigned 64 bit integer

    Args:
        data (bytes)

    Returns:
        int
    """
    if endianness is True:
        value = unpack_from('>Q', data, offset)[0]  # big-endian
    elif endianness is False:
        value = unpack_from('<Q', data, offset)[0]  # little-endian
    elif endianness is None:
        value = unpack_from('Q', data, offset)[0]  # machine byte order
    else:
        raise Exception('Invalid value "{}" for endianness given'.format(endianness))
    return value
