from crypto.transactions.deserializer import Deserializer
from crypto.transactions.types.transfer import Transfer
from crypto.transactions.types.vote import Vote
from crypto.transactions.types.unvote import Unvote
from crypto.transactions.types.validator_registration import ValidatorRegistration
from crypto.transactions.types.validator_resignation import ValidatorResignation

def assert_deserialized(fixture, keys):
    deserializer = Deserializer.new(fixture['serialized'])
    transaction = deserializer.deserialize()
    for key in keys:
        assert transaction.data[key] == fixture['data'][key], f"Mismatch in {key}"
    assert transaction.serialize().hex() == fixture['serialized']
    assert transaction.verify()
    return transaction

def test_deserialize_transfer(load_transaction_fixture):
    fixture = load_transaction_fixture('transfer')
    transaction = assert_deserialized(fixture, ['id', 'nonce', 'gasPrice', 'gasLimit', 'value', 'v', 'r', 's'])

    assert isinstance(transaction, Transfer)
    assert transaction.data['value'] == '100000000'

def test_deserialize_vote(load_transaction_fixture):
    fixture = load_transaction_fixture('vote')
    transaction = assert_deserialized(fixture, ['id', 'nonce', 'gasPrice', 'gasLimit', 'v', 'r', 's'])

    assert isinstance(transaction, Vote)
    assert transaction.data['vote'].lower() == '0xc3bbe9b1cee1ff85ad72b87414b0e9b7f2366763'
    assert transaction.data['id'] == '991a3a63dc47be84d7982acb4c2aae488191373f31b8097e07d3ad95c0997e69'

def test_deserialize_unvote(load_transaction_fixture):
    fixture = load_transaction_fixture('unvote')
    transaction = assert_deserialized(fixture, ['id', 'nonce', 'gasPrice', 'gasLimit', 'v', 'r', 's'])

    assert isinstance(transaction, Unvote)

def test_deserialize_validator_registration(load_transaction_fixture):
    fixture = load_transaction_fixture('validator-registration')
    transaction = assert_deserialized(fixture, ['id', 'nonce', 'gasPrice', 'gasLimit', 'v', 'r', 's'])

    assert isinstance(transaction, ValidatorRegistration)

def test_deserialize_validator_resignation(load_transaction_fixture):
    fixture = load_transaction_fixture('validator-resignation')
    transaction = assert_deserialized(fixture, ['id', 'nonce', 'gasPrice', 'gasLimit', 'v', 'r', 's'])

    assert isinstance(transaction, ValidatorResignation)
