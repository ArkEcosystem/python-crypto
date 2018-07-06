class CryptoException(Exception):
    pass


class SerializerException(CryptoException):
    """Raised when there's a serializer related issue"""
