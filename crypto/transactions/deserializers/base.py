class BaseDeserializer(object):

    serialized = None
    asset_offset = None
    transaction = None

    def __init__(self, serialized, asset_offset, transaction):
        self.serialized = serialized
        self.asset_offset = asset_offset
        self.transaction = transaction

    def deserialize(self):
        raise NotImplementedError
