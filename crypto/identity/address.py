import hashlib
from binascii import unhexlify

from base58 import b58encode_check

from binary.unsigned_integer.writer import write_bit8

from crypto.conf import get_network
from crypto.identity.keys import private_key_from_passphrase, compress_ecdsa_public_key


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

    ripemd160 = hashlib.new('ripemd160', unhexlify(public_key))
    seed = write_bit8(network_version) + ripemd160.digest()
    return b58encode_check(seed)


def address_from_private_key(private_key, network_version=None):
    """Get an address from private key

    Args:
        private_key (string):
        network_version (int, optional):

    Returns:
        TYPE: Description
    """
    if not network_version:
        network = get_network()
        network_version = network['version']

    public_key = compress_ecdsa_public_key(unhexlify(private_key))
    ripemd160 = hashlib.new('ripemd160', unhexlify(public_key))
    seed = write_bit8(network_version) + ripemd160.digest()
    return b58encode_check(seed)


def address_from_passphrase(passphrase, network_version=None):
    """Get an address from passphrase

    Args:
        passphrase (bytes):
        network_version (int, optional):

    Returns:
        TYPE: Description
    """
    if not network_version:
        network = get_network()
        network_version = network['version']

    private_key = hashlib.sha256(passphrase).hexdigest()
    address = address_from_private_key(private_key)
    return address
