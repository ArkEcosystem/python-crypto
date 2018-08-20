class ArkCryptoException(Exception):
    pass


class ArkSerializerException(ArkCryptoException):
    """Raised when there's a serializer related issue"""


class ArkNetworkSettingsException(ArkCryptoException):
    """Raised when a curve is too short for a digest"""


class ArkInvalidTransaction(ArkCryptoException):
    """Raised when transaction is not valid"""
