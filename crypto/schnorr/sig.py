# -*- encoding:utf-8 -*-

"""
Advanced signature manipulation. It is the recomended module to manually issue
signatures for ark blockchain and forks.

Variables:
  - ``privateKey`` (:class:`str`): hexlified private key
  - ``publicKey`` (:class:`str`):  hexlified compressed - encoded public key
  - ``message`` (:class:`str`):    message to sign as string
"""

from secp256k1 import *
from utils import unhexlify


class Signature(list):
    r = property(
        lambda cls: list.__getitem__(cls, 0),
        None, None, ""
    )

    s = property(
        lambda cls: list.__getitem__(cls, 1),
        None, None, ""
    )

    der = property(
        lambda cls: cls._der_getter(),
        lambda cls, v: setattr(cls, "_der", v),
        None, ""
    )

    raw = property(
        lambda cls: cls._raw_getter(),
        lambda cls, v: setattr(cls, "_raw", v),
        None, ""
    )

    def __init__(self, *rs):
        list.__init__(self, [int(e) for e in rs])

    def _der_getter(cls):
        if not hasattr(cls, "_der"):
            setattr(cls, "_der", der_from_sig(*cls))
        return getattr(cls, "_der")

    def _raw_getter(cls):
        if not hasattr(cls, "_raw"):
            setattr(
                cls, "_raw",
                bytes_from_int(cls[0]) +
                bytes_from_int(cls[1])
            )
        return getattr(cls, "_raw")

    def b410_schnorr_verify(self, message, publicKey):
        return bcrypto410_verify(
            hash_sha256(message),
            Point.decode(unhexlify(publicKey)).encode(),
            self.raw
        )

    def schnorr_verify(self, message, publicKey):
        return verify(
            hash_sha256(message),
            bytes_from_point(
                Point.decode(unhexlify(publicKey))
            ),
            self.raw
        )

    @staticmethod
    def from_raw(raw):
        length = len(raw) // 2
        sig = Signature(
            int_from_bytes(raw[:length]),
            int_from_bytes(raw[length:]),
        )
        sig._raw = raw
        return sig

    @staticmethod
    def from_der(der):
        sig = Signature(*sig_from_der(der))
        sig._der = der
        return sig

    @staticmethod
    def b410_schnorr_sign(message, privateKey):
        return Signature.from_raw(
            bcrypto410_sign(
                hash_sha256(message), unhexlify(privateKey)
            )
        )

    @staticmethod
    def schnorr_sign(message, privateKey):
        return Signature.from_raw(
            sign(
                hash_sha256(message), unhexlify(privateKey)
            )
        )