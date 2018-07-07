import pytest

from crypto.serializer import Serializer


@pytest.mark.skip(reason='not implemented')
def test_serializer(transaction_type_8):
    # todo: must implement fallback method for fetching network version in serializer.py
    result = Serializer(transaction_type_8).serialize()
    assert result == transaction_type_8['serialized']
