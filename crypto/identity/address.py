import hashlib
from binascii import unhexlify

from base58 import b58encode_check

from binary.unsigned_integer.writer import write_bit8

from crypto.conf import get_network


def address_from_public_key(public_key, network_version=None):
    """Get an address from a public key

    Args:
        public_key (bytes):
        network_version (int, optional):

    Returns:
        bytes:
    """
    if not network_version:
        network = get_network()
        network_version = network['version']

    network_version = network_version
    ripemd160 = hashlib.new('ripemd160', unhexlify(public_key))
    seed = write_bit8(network_version) + ripemd160.digest()
    return b58encode_check(seed)
