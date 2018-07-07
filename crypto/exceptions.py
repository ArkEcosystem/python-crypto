class ArkCryptoException(Exception):
    pass


class ArkSerializerException(ArkCryptoException):
    """Raised when there's a serializer related issue"""
