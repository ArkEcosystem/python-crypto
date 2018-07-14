from binascii import hexlify
from hashlib import sha256


from ecdsa import SECP256k1, SigningKey
from ecdsa.util import number_to_string


def privat_key_from_secret(secret):
    """Get a private key from a given secret (aka passphrase)

    Args:
        secret (bytes): bytes string

    Returns:
        bytes: private key
    """
    private_key = sha256(secret)
    return private_key.hexdigest().encode()


def public_key_from_secret(secret):
    """Get a public key from a given secret (aka passphrase)

    Args:
        secret (bytes): bytes string

    Returns:
        bytes: public key
    """
    private_key = sha256(secret)
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


def uncompress_ecdsa_public_key(public_key):
    """
    Uncompressed public key is:
    0x04 + x-coordinate + y-coordinate
    Compressed public key is:
    0x02 + x-coordinate if y is even
    0x03 + x-coordinate if y is odd
    y^2 mod p = (x^3 + 7) mod p
    read more : https://bitcointalk.org/index.php?topic=644919.msg7205689#msg7205689
    """
    p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
    y_parity = int(public_key[:2]) - 2
    x = int(public_key[2:], 16)
    a = (pow(x, 3, p) + 7) % p
    y = pow(a, (p + 1) // 4, p)
    if y % 2 != y_parity:
        y = -y % p
    # return result as der signature (no 0x04 preffix)
    return '{:x}{:x}'.format(x, y)
