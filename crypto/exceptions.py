class ArkCryptoException(Exception):
    pass


class ArkSerializerException(ArkCryptoException):
    """Raised when there's a serializer related issue"""


class ArkInvalidTransaction(ArkCryptoException):
    """Raised when transaction is not valid"""


class InvalidUsernameException(Exception):
    """Raised when username is invalid"""
