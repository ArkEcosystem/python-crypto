from crypto.identity.private_key import PrivateKey
from crypto.transactions.deserializer import Deserializer

def test_compute_id_of_transaction(load_transaction_fixture):
    transaction = Deserializer.new(load_transaction_fixture('transfer')['serialized']).deserialize()
    assert len(transaction.get_id()) == 64

def test_sign_transaction_with_passphrase(load_transaction_fixture):
    private_key = PrivateKey.from_passphrase('this is a top secret passphrase')
    transaction = Deserializer.new(load_transaction_fixture('transfer')['serialized']).deserialize()

    transaction.data['v'] = ''
    transaction.data['r'] = ''
    transaction.data['s'] = ''

    assert 'v' not in transaction.data or transaction.data['v'] == ''
    assert 'r' not in transaction.data or transaction.data['r'] == ''
    assert 's' not in transaction.data or transaction.data['s'] == ''

    transaction.sign(private_key)

    assert transaction.data['v'] != ''
    assert transaction.data['r'] != ''
    assert transaction.data['s'] != ''

def test_verify_transaction(load_transaction_fixture):
    transaction = Deserializer.new(load_transaction_fixture('transfer')['serialized']).deserialize();
    assert transaction.verify()

def test_transaction_to_bytes(load_transaction_fixture):
    transaction = Deserializer.new(load_transaction_fixture('transfer')['serialized']).deserialize();
    actual = transaction.get_bytes()
    assert isinstance(actual, bytes)

def test_transaction_to_array(load_transaction_fixture):
    transaction = Deserializer.new(load_transaction_fixture('transfer')['serialized']).deserialize();
    actual = transaction.to_dict()
    assert isinstance(actual, dict)

def test_transaction_to_json(load_transaction_fixture):
    transaction = Deserializer.new(load_transaction_fixture('transfer')['serialized']).deserialize();
    actual = transaction.to_json()
    assert isinstance(actual, str)
