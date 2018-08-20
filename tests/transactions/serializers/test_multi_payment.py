import pytest

from crypto.transactions.serializer import Serializer


@pytest.mark.skip(reason='not implemented - missing fixture')
def test_serializer(transaction_type_7):
    result = Serializer(transaction_type_7).serialize()
    assert result == transaction_type_7['serialized']
