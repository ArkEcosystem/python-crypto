from crypto.utils.rlp_encoder import RlpEncoder
from crypto.utils.transaction_utils import TransactionUtils


def test_encode_function_call(load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/transfer')

    # Calls RlpEncoder.encode() with the given transaction
    transaction_hash = TransactionUtils.to_buffer(fixture['data'])

    assert transaction_hash.decode() ==  fixture['serialized']

def test_encoding_str():
    encoded = RlpEncoder.encode('testing')

    assert encoded == '8774657374696e67'

def test_encoding_bytes():
    encoded = RlpEncoder.encode(b'testing')

    assert encoded == '8774657374696e67'

def test_encoding_list():
    encoded = RlpEncoder.encode(['testing'])

    assert encoded == 'c88774657374696e67'

def test_encoding_int():
    encoded = RlpEncoder.encode('123456')

    assert encoded == '86313233343536'
