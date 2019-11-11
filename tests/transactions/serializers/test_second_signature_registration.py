from crypto.transactions.serializer import Serializer


def test_serializer(transaction_type_1):
    print(transaction_type_1)
    result = Serializer(transaction_type_1).serialize(False, False)
    print(result)
    assert result == transaction_type_1['serialized']
