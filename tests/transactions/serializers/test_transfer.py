from crypto.conf import use_network
from crypto.transactions.serializer import Serializer


def test_serializer(transaction_type_0):
    use_network('devnet')
    result = Serializer(transaction_type_0).serialize()
    assert result == transaction_type_0['serialized']
