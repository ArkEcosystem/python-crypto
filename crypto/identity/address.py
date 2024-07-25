import hashlib
from binascii import unhexlify

from crypto.identity.private_key import PrivateKey

from Cryptodome.Hash import RIPEMD160, keccak
from coincurve import PrivateKey, PublicKey

def get_checksum_address(address):
    """Get checksum address

    Args:
        address (str): address to get checksum

    Returns:
        str: checksum address
    """
    address = address.lower()

    chars = list(address[2:])

    expanded = bytearray(40)
    for i in range(40):
        expanded[i] = ord(chars[i])

    hashed = keccak.new(data=bytes(expanded), digest_bits=256).digest()

    for i in range(0, 40, 2):
        if (hashed[i >> 1] >> 4) >= 8:
            chars[i] = chars[i].upper()
        if (hashed[i >> 1] & 0x0F) >= 8:
            chars[i + 1] = chars[i + 1].upper()

    return "0x" + ''.join(chars)

def address_from_public_key(public_key):
    """Get an address from a public key

    Args:
        public_key (str):

    Returns:
        str: address
    """

    public_key = PublicKey(bytes.fromhex(public_key)).format(compressed=False)[1:]

    keccak_hash = keccak.new(
        data=bytearray.fromhex(public_key.hex()),
        digest_bits=256,
    )

    return get_checksum_address(unhexlify(keccak_hash.hexdigest()[22:]).hex())


def address_from_private_key(private_key):
    """Get an address from private key

    Args:
        private_key (string):

    Returns:
        TYPE: Description
    """
    private_key = PrivateKey.from_hex(private_key)

    return address_from_public_key(private_key.public_key.format(compressed=False).hex())


def address_from_passphrase(passphrase):
    """Get an address from passphrase

    Args:
        passphrase (str):
        network_version (int, optional):

    Returns:
        string: address
    """
    private_key = hashlib.sha256(passphrase.encode()).hexdigest()
    address = address_from_private_key(private_key)
    return address
