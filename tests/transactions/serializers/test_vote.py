from crypto.transactions.serializer import Serializer


def test_serializer(transaction_type_3):
    result = Serializer(transaction_type_3).serialize(False, True)
    assert result == transaction_type_3['serialized']
