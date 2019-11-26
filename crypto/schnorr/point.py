from .secp256k1 import encoded_from_point, point_from_encoded

p = int(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F)

def x(P):
    """
    Return :class:`P.x` or :class:`P[0]`.
    Args:
        P (:class:`list`): ``secp256k1`` point
    Returns:
        :class:`int`: x
    """
    return P[0]

def y(P):
    """
    Return :class:`P.y` or :class:`P[1]`.
    Args:
        P (:class:`list`): ``secp256k1`` point
    Returns:
        :class:`int`: y
    """
    return P[1]

def y_from_x(x):
    """
    Compute :class:`P.y` from :class:`P.x` according to ``y²=x³+7``.
    """
    y_sq = (pow(x, 3, p) + 7) % p
    y = pow(y_sq, (p + 1) // 4, p)
    if pow(y, 2, p) != y_sq:
        return None
    return y

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
        raise ValueError("One of the point is not on the curve")
    if (P1 == P2):
        lam = (3 * x(P1) * x(P1) * pow(2 * y(P1), p - 2, p)) % p
    else:
        lam = ((y(P2) - y(P1)) * pow(x(P2) - x(P1), p - 2, p)) % p
    x3 = (lam * lam - x(P1) - x(P2)) % p
    return [x3, (lam * (x(P1) - x3) - y(P1)) % p]

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

class Point(list):
    """
    ``secp256k1`` point . Initialization can be done with sole ``x`` value.
    :class:`Point` overrides ``*`` and ``+`` operators which accepts
    :class:`list` as argument and returns :class:`Point`. It extends
    :class:`list` and allows item access using ``__getattr__``/``__setattr__``
    operators.
    >>> from dposlib.ark import secp256k1
    >>> G = secp256k1.Point(0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D9\
59F2815B16F81798)
    >>> G
    [5506626302227734366957871889516853432625060345377759417550018736038911672\
9240, 326705100207588169780830851305070431844712733806592432759389043357573374\
82424]
    >>> G.y
    32670510020758816978083085130507043184471273380659243275938904335757337482\
424
    >>> G + G
    [8956589192654700423125292042593569236064414582962220983368432991329718898\
6597, 121583992996938303229678086127133986361553678870416281767988719547883716\
53930]
    >>> 2 * G
    [8956589192654700423125292042593569236064414582962220983368432991329718898\
6597, 121583992996938303229678086127133986361553678870416281767988719547883716\
53930]
    >>> type(2 * G)
    <class 'dposlib.ark.secp256k1.Point'>
    Parameters:
        x (:class:`int`): abscissa
        y (:class:`int`): ordinate
    """

    x = property(
        lambda cls: list.__getitem__(cls, 0),
        lambda cls, v: [
            list.__setitem__(cls, 0, int(v)),
            list.__setitem__(cls, 1, y_from_x(int(v)))
        ],
        None, ""
    )
    y = property(
        lambda cls: list.__getitem__(cls, 1),
        None, None, ""
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
        See :func:`dposlib.ark.secp256k1.point_from_encoded`.
        """
        return Point(*point_from_encoded(pubkey))

    def encode(self):
        """
        See :func:`dposlib.ark.secp256k1.encoded_from_point`.
        """
        return encoded_from_point(self)