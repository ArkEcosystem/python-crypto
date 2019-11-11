from crypto.transactions.serializer import Serializer


def test_serializer(transaction_type_1):
    result = Serializer(transaction_type_1).serialize(False, False)
    assert result == transaction_type_1['serialized']
