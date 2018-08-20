import pytest

from crypto.transactions.serializer import Serializer


@pytest.mark.skip(reason='not implemented - missing fixture')
def test_serializer(transaction_type_6):
    result = Serializer(transaction_type_6).serialize()
    assert result == transaction_type_6['serialized']
