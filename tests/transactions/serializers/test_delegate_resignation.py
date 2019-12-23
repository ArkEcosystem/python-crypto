from crypto.transactions.serializer import Serializer


def test_serializer(transaction_type_7):
    result = Serializer(transaction_type_7).serialize(False, True)
    assert result == transaction_type_7['serialized']
