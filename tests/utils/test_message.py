import json

from crypto.utils.message import Message

def test_verify_with_publicKey(load_transaction_fixture):
    fixture = load_transaction_fixture('message-sign')

    result = Message(
        message=fixture['message'],
        signature=fixture['signature'],
        public_key=fixture['publicKey'],
    )

    isVerified = result.verify()

    assert isVerified is True

def test_message_sign_verification(load_transaction_fixture, passphrase):
    fixture = load_transaction_fixture('message-sign')

    message: Message = Message.sign(fixture['message'], passphrase)

    assert message.signature.decode() == fixture['signature']
    assert message.public_key.decode() == fixture['publicKey']
    assert message.message.decode() == fixture['message']

    isVerified = message.verify()

    assert isVerified is True

def test_to_dict(load_transaction_fixture):
    fixture = load_transaction_fixture('message-sign')

    result = Message(
        message=fixture['message'],
        signature=fixture['signature'],
        public_key=fixture['publicKey'],
    )

    data = result.to_dict()

    assert data['signature'] == fixture['signature']
    assert data['public_key'] == fixture['publicKey']
    assert data['message'] == fixture['message']

def test_to_json(load_transaction_fixture):
    fixture = load_transaction_fixture('message-sign')

    result = Message(
        message=fixture['message'],
        signature=fixture['signature'],
        public_key=fixture['publicKey'],
    )

    json_data = result.to_json()
    data = json.loads(json_data)

    assert data['signature'] == fixture['signature']
    assert data['public_key'] == fixture['publicKey']
    assert data['message'] == fixture['message']
