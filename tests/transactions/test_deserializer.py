from crypto.transactions.deserializer import Deserializer
from crypto.transactions.types.transfer import Transfer
from crypto.transactions.types.username_registration import UsernameRegistration
from crypto.transactions.types.username_resignation import UsernameResignation
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
    assert transaction.data['id'] == fixture['data']['id']

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

def test_deserialize_username_registration(load_transaction_fixture):
    fixture = load_transaction_fixture('username-registration')
    transaction = assert_deserialized(fixture, ['id', 'nonce', 'gasPrice', 'gasLimit', 'v', 'r', 's'])

    assert isinstance(transaction, UsernameRegistration)

def test_deserialize_username_resignation(load_transaction_fixture):
    fixture = load_transaction_fixture('username-resignation')
    transaction = assert_deserialized(fixture, ['id', 'nonce', 'gasPrice', 'gasLimit', 'v', 'r', 's'])

    assert isinstance(transaction, UsernameResignation)

def test_parse_number():
    assert Deserializer.parse_number('0x01') == 1
    assert Deserializer.parse_number('0x0100') == 256
    assert Deserializer.parse_number('0x010000') == 65536
    assert Deserializer.parse_number('0x') == 0

def test_parse_big_number():
    assert Deserializer.parse_big_number('0x01') == '1'
    assert Deserializer.parse_big_number('0x0100') == '256'
    assert Deserializer.parse_big_number('0x010000') == '65536'
    assert Deserializer.parse_big_number('0x') == '0'
    assert Deserializer.parse_big_number('0x52B7D2DCC80CD2E4000000') == '100000000000000000000000000'

def test_parse_hex():
    assert Deserializer.parse_hex('0x01') == '01'
    assert Deserializer.parse_hex('0x0100') == '0100'
    assert Deserializer.parse_hex('0x010000') == '010000'
    assert Deserializer.parse_hex('0x') == ''
    assert Deserializer.parse_hex('0x52B7D2DCC80CD2E4000000') == '52B7D2DCC80CD2E4000000'

def test_parse_address():
    assert Deserializer.parse_address('0x52B7D2DCC80CD2E4000000') == '0x52B7D2DCC80CD2E4000000'
    assert Deserializer.parse_address('0x') == None
