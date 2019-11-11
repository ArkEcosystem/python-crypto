from crypto.transactions.serializer import Serializer


def test_serializer(transaction_type_4):
    print(transaction_type_4['serialized'])
    result = Serializer(transaction_type_4).serialize(False, False)
    print("RESULT")
    print(result)
    assert result == transaction_type_4['serialized']
