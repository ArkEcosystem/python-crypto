class BaseDeserializer(object):

    serialized = None
    asset_offset = None
    transaction = None

    def __init__(self, serialized, asset_offset, transaction):
        self.serialized = serialized
        self.asset_offset = asset_offset
        self.transaction = transaction

    def parse_signatures(self, start_offset):
        return self.transaction.parse_signatures(self.serialized, start_offset)

    def deserialize(self):
        raise NotImplementedError
