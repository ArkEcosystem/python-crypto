class BaseSerializer(object):

    transaction = None
    bytes_data = None

    def __init__(self, transaction, bytes_data=bytes()):
        self.transaction = transaction
        self.bytes_data = bytes_data

    def serialize(self):
        raise NotImplementedError
