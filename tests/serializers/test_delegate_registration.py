from crypto.serializer import Serializer


def test_serializer(transaction_type_2):
    result = Serializer(transaction_type_2).serialize()
    assert result == transaction_type_2['serialized']
