import pytest

from crypto.conf import use_network
from crypto.serializer import Serializer


@pytest.mark.skip(reason='not implemented - missing fixture')
def test_serializer(transaction_type_5):
    use_network('devnet')
    result = Serializer(transaction_type_5).serialize()
    assert result == transaction_type_5['serialized']
