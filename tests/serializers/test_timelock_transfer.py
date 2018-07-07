import pytest

from crypto.serializer import Serializer


@pytest.mark.skip(reason='not implemented')
def test_serializer(transaction_type_6):
    # todo: must implement fallback method for fetching network version in serializer.py
    result = Serializer(transaction_type_6).serialize()
    assert result == transaction_type_6['serialized']
