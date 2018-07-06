from crypto.serializer import Serializer


def test_serializer(transaction_type_3):
    result = Serializer(transaction_type_3).serialize()
    assert result.hex() == transaction_type_3['serialized']
