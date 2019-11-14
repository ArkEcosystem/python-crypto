import pytest

from crypto.transactions.serializer import Serializer


def test_serializer(transaction_type_6):
    print("INSIDE TEST")
    print("FIXTURE :")
    print(transaction_type_6)
    result = Serializer(transaction_type_6).serialize(False, True)
    print("EXPECTED")
    print(transaction_type_6['serialized'])
    print("RESULT")
    print(result)
    assert result == transaction_type_6['serialized']
