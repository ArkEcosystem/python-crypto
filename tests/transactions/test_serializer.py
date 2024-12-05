from crypto.transactions.serializer import Serializer
from crypto.transactions.types.transfer import Transfer
from crypto.transactions.types.vote import Vote
from crypto.transactions.types.unvote import Unvote
from crypto.transactions.types.validator_registration import ValidatorRegistration
from crypto.transactions.types.validator_resignation import ValidatorResignation

def test_transfer_serialization(load_transaction_fixture):
    fixture = load_transaction_fixture('transfer')
    transaction = Transfer(fixture['data'])
    serializer = Serializer.new(transaction)
    assert serializer.serialize().hex() == fixture['serialized']

def test_vote_serialization(load_transaction_fixture):
    fixture = load_transaction_fixture('vote')
    transaction = Vote(fixture['data'])
    print(f"transaction: {transaction.data}")
    serializer = Serializer.new(transaction)
    assert serializer.serialize().hex() == fixture['serialized']

def test_unvote_serialization(load_transaction_fixture):
    fixture = load_transaction_fixture('unvote')
    transaction = Unvote(fixture['data'])
    serializer = Serializer.new(transaction)
    assert serializer.serialize().hex() == fixture['serialized']

def test_validator_registration_serialization(load_transaction_fixture):
    fixture = load_transaction_fixture('validator-registration')
    transaction = ValidatorRegistration(fixture['data'])
    serializer = Serializer.new(transaction)
    assert serializer.serialize().hex() == fixture['serialized']

def test_validator_resignation_serialization(load_transaction_fixture):
    fixture = load_transaction_fixture('validator-resignation')
    transaction = ValidatorResignation(fixture['data'])
    serializer = Serializer.new(transaction)
    assert serializer.serialize().hex() == fixture['serialized']