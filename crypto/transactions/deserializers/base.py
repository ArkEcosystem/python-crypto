from crypto.transactions.transaction import Transaction

class BaseDeserializer(object):
    serialized: bytes
    asset_offset: int
    transaction: Transaction

    def __init__(self, serialized: bytes, asset_offset: int, transaction: Transaction):
        self.serialized = serialized
        self.asset_offset = asset_offset
        self.transaction = transaction

    def deserialize(self):
        raise NotImplementedError
