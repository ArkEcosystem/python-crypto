class BaseSerializer(object):
    transaction: dict
    bytes_data: bytes

    def __init__(self, transaction: dict, bytes_data: bytes = bytes()):
        self.transaction = transaction
        self.bytes_data = bytes_data

    def serialize(self):
        raise NotImplementedError
