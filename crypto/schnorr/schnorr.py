# From Toons implementation
# see here https://github.com/Moustikitos/dpos/blob/master/dposlib/ark/secp256k1/schnorr.py

import hashlib
from binascii import unhexlify
from builtins import int

p = int(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F)
n = int(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141)


def point_from_encoded(pubkey):
    """
    Decode and decompress a ``secp256k1`` point.
    Args:
        pubkey (:class:`bytes`): compressed and encoded point
    Returns:
        :class:`list`: ``secp256k1`` point
    """
    pubkey = bytearray(pubkey)
    x = int_from_bytes(pubkey[1:])
    y = y_from_x(x)
    if y is None:
        raise ValueError('Point not on ``secp256k1`` curve')
    elif y % 2 != pubkey[0] - 2:
        y = -y % p
    return [x, y]


def y_from_x(x):
    """
    Compute :class:`P.y` from :class:`P.x` according to ``y²=x³+7``.
    """
    y_sq = (pow(x, 3, p) + 7) % p
    y = pow(y_sq, (p + 1) // 4, p)
    if pow(y, 2, p) != y_sq:
        return None
    return y


class Point(list):
    """
    ``secp256k1`` point . Initialization can be done with sole ``x`` value.
    :class:`Point` overrides ``*`` and ``+`` operators which accepts
    :class:`list` as argument and returns :class:`Point`. It extends
    :class:`list` and allows item access using ``__getattr__``/``__setattr__``
    operators.
    """

    x = property(
        lambda cls: list.__getitem__(cls, 0),
        lambda cls, v: [
            list.__setitem__(cls, 0, int(v)),
            list.__setitem__(cls, 1, y_from_x(int(v)))
        ],
        None, ''
    )
    y = property(
        lambda cls: list.__getitem__(cls, 1),
        None, None, ''
    )

    def __init__(self, *xy):
        if len(xy) == 0:
            xy = (0, None)
        elif len(xy) == 1:
            xy += (y_from_x(int(xy[0])), )
        list.__init__(self, [int(e) if e is not None else e for e in xy[:2]])

    def __mul__(self, k):
        if isinstance(k, int):
            return Point(*point_mul(self, k))
        else:
            raise TypeError("'%s' should be an int" % k)
    __rmul__ = __mul__

    def __add__(self, P):
        if isinstance(P, list):
            return Point(*point_add(self, P))
        else:
            raise TypeError("'%s' should be a 2-int-length list" % P)
    __radd__ = __add__

    @staticmethod
    def decode(pubkey):
        """
        Decode and decompress a ``secp256k1`` point.
        """
        return Point(*point_from_encoded(pubkey))

    def encode(self):
        """
        Decode and decompress a ``secp256k1`` point.
        """
        return encoded_from_point(self)


G = Point(0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798)


def point_add(P1, P2):
    """
    Add ``secp256k1`` points.
    Args:
        P1 (:class:`list`): first ``secp256k1`` point
        P2 (:class:`list`): second ``secp256k1`` point
    Returns:
        :class:`list`: ``secp256k1`` point
    """
    if (P1 is None):
        return P2
    if (P2 is None):
        return P1
    if (x(P1) == x(P2) and y(P1) != y(P2)):
        raise ValueError('One of the point is not on the curve')
    if (P1 == P2):
        lam = (3 * x(P1) * x(P1) * pow(2 * y(P1), p - 2, p)) % p
    else:
        lam = ((y(P2) - y(P1)) * pow(x(P2) - x(P1), p - 2, p)) % p
    x3 = (lam * lam - x(P1) - x(P2)) % p
    return [x3, (lam * (x(P1) - x3) - y(P1)) % p]


def bcrypto410_verify(msg, pubkey, sig):
    if len(msg) != 32:
        raise ValueError('The message must be a 32-byte array.')
    if len(sig) != 64:
        raise ValueError('The signature must be a 64-byte array.')

    P = Point.decode(pubkey)
    r, s = int_from_bytes(sig[:32]), int_from_bytes(sig[32:])
    if r >= p or s >= n:
        return False

    e = int_from_bytes(hash_sha256(sig[0:32] + pubkey + msg)) % n
    R = Point(*(G*s + point_mul(P, n-e)))  # P*(n-e) does not work...
    if R is None or not is_quad(R.y) or R.x != r:
        return False
    return True


def b410_schnorr_verify(message, publicKey, signature):
    return bcrypto410_verify(
        hash_sha256(message),
        Point.decode(unhexlify(publicKey)).encode(),
        unhexlify(signature)
    )


def x(P):
    """
    Return :class:`P.x` or :class:`P[0]`.
    Args:
        P (:class:`list`): ``secp256k1`` point
    Returns:
        :class:`int`: x
    """
    return P[0]


def bytes_from_int(x):
    return int(x).to_bytes(32, byteorder='big')


def int_from_bytes(b):
    return int.from_bytes(b, byteorder='big')


def jacobi(x):
    return pow(x, (p - 1) // 2, p)


def is_quad(x):
    return jacobi(x) == 1


def hash_sha256(b):
    """
    Args:
        b (:class:`bytes` or :class:`str`): sequence to be hashed
    Returns:
        :class:`bytes`: sha256 hash
    """
    return hashlib.sha256(
        b if isinstance(b, bytes) else b.encode('utf-8')
    ).digest()


def point_mul(P, n):
    """
    Multiply ``secp256k1`` point with scalar.
    Args:
        P (:class:`list`): ``secp256k1`` point
        n (:class:`int`): scalar
    Returns:
        :class:`list`: ``secp256k1`` point
    """
    R = None
    for i in range(256):
        if ((n >> i) & 1):
            R = point_add(R, P)
        P = point_add(P, P)
    return R


def y(P):
    """
    Return :class:`P.y` or :class:`P[1]`.

    Args:
        P (:class:`list`): ``secp256k1`` point
    Returns:
        :class:`int`: y
    """
    return P[1]


def encoded_from_point(P):
    """
    Encode and compress a ``secp256k1`` point:
      * ``bytes(2) || bytes(x)`` if y is even
      * ``bytes(3) || bytes(x)`` if y is odd

    Args:
        P (:class:`list`): ``secp256k1`` point
    Returns:
        :class:`bytes`: compressed and encoded point
    """
    return (b'\x03' if y(P) & 1 else b'\x02') + bytes_from_int(x(P))


# https://github.com/bcoin-org/bcrypto/blob/v4.1.0/lib/js/schnorr.js
def bcrypto410_sign(msg, seckey0):
    if len(msg) != 32:
        raise ValueError('The message must be a 32-byte array.')

    seckey = int_from_bytes(seckey0)
    if not (1 <= seckey <= n - 1):
        raise ValueError(
            'The secret key must be an integer in the range 1..n-1.'
        )

    k0 = int_from_bytes(hash_sha256(seckey0 + msg)) % n
    if k0 == 0:
        raise RuntimeError(
            'Failure. This happens only with negligible probability.'
        )

    R = G * k0
    Rraw = bytes_from_int(R.x)
    e = int_from_bytes(
        hash_sha256(Rraw + encoded_from_point(G*seckey) + msg)
    ) % n

    seckey %= n
    k0 %= n
    k = n - k0 if not is_quad(R.y) else k0

    s = (k + e * seckey) % n
    s %= n

    return Rraw + bytes_from_int(s)
