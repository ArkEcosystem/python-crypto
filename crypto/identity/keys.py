from binascii import hexlify
from hashlib import sha256


from ecdsa import SECP256k1, SigningKey
from ecdsa.util import number_to_string


def private_key_from_passphrase(passphrase):
    """Get a private key from a given passphrase

    Args:
        passphrase (bytes): bytes string

    Returns:
        bytes: private key
    """
    private_key = sha256(passphrase)
    return private_key.hexdigest().encode()


def public_key_from_passphrase(passphrase):
    """Get a public key from a given passphrase

    Args:
        passphrase (bytes): bytes string

    Returns:
        bytes: public key
    """
    private_key = sha256(passphrase)
    public_key = compress_ecdsa_public_key(private_key.digest())
    return public_key.encode()


def compress_ecdsa_public_key(private_key):
    """ECDSA compressed public key

    Args:
        private_key (bytes): private key

    Returns:
        bytes: compressed ecdsa public key
    """
    order = SigningKey.from_string(private_key, curve=SECP256k1).curve.generator.order()
    point = SigningKey.from_string(private_key, curve=SECP256k1).verifying_key.pubkey.point
    x_str = number_to_string(point.x(), order)
    compressed = hexlify(chr(2 + (point.y() & 1)).encode() + x_str)
    return compressed.decode()
