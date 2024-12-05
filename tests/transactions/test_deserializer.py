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
    transaction = assert_deserialized(fixture, ['id', 'nonce', 'gasPrice', 'gasLimit', 'value', 'signature'])
    
    assert isinstance(transaction, Transfer)
    assert transaction.data['value'] == '10000000000000000000'

def test_deserialize_vote(load_transaction_fixture):
    fixture = load_transaction_fixture('vote')
    transaction = assert_deserialized(fixture, ['id', 'nonce', 'gasPrice', 'gasLimit', 'signature'])
    
    assert isinstance(transaction, Vote)
    assert transaction.data['vote'] == '0x512F366D524157BcF734546eB29a6d687B762255'
    assert transaction.data['id'] == '749744e0d689c46e37ff2993a984599eac4989a9ef0028337b335c9d43abf936'

def test_deserialize_unvote(load_transaction_fixture):
    fixture = load_transaction_fixture('unvote')
    transaction = assert_deserialized(fixture, ['id', 'nonce', 'gasPrice', 'gasLimit', 'signature'])
    
    assert isinstance(transaction, Unvote)

def test_deserialize_validator_registration(load_transaction_fixture):
    fixture = load_transaction_fixture('validator-registration')
    transaction = assert_deserialized(fixture, ['id', 'nonce', 'gasPrice', 'gasLimit', 'signature'])
    
    assert isinstance(transaction, ValidatorRegistration)

def test_deserialize_validator_resignation(load_transaction_fixture):
    fixture = load_transaction_fixture('validator-resignation')
    transaction = assert_deserialized(fixture, ['id', 'nonce', 'gasPrice', 'gasLimit', 'signature'])
    
    assert isinstance(transaction, ValidatorResignation)