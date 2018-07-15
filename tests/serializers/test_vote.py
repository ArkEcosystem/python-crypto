from crypto.conf import use_network
from crypto.serializer import Serializer


def test_serializer(transaction_type_3):
    use_network('devnet')
    result = Serializer(transaction_type_3).serialize()
    assert result == transaction_type_3['serialized']
