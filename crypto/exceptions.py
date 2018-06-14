class ArkCryptoException(Exception):
    pass


class ArkSerializerException(ArkCryptoException):
    """Raised when there's a serializer related issue"""


class ArkBadSignatureException(ArkCryptoException):
    """Raised when a signature is not valid"""


class ArkBadDigestException(ArkCryptoException):
    """Raised when a curve is too short for a digest"""


class ArkNetworkSettingsException(ArkCryptoException):
    """Raised when a curve is too short for a digest"""
