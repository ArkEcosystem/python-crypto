import pytest

from crypto.transactions.serializer import Serializer


def test_serializer(transaction_type_5):
    print("INSIDE")
    result = Serializer(transaction_type_5).serialize(False, True)
    print("FIXTURE")
    print(transaction_type_5)
    print("RESULT")
    print(result)
    assert result == transaction_type_5['serialized']
