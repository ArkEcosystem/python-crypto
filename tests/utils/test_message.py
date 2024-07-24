import json

from crypto.utils.message import Message

def test_verify_with_publicKey(message):
    result = Message(
        message=message['message'],
        signature=message['signature'],
        public_key=message['publicKey'],
    )

    isVerified = result.verify()

    assert isVerified is True

def test_message_sign_verification(message):
    message: Message = Message.sign(message['message'], message['passphrase'])

    isVerified = message.verify()

    assert isVerified is True

def test_to_dict(message):
    result = Message(
        message=message['message'],
        signature=message['signature'],
        public_key=message['publicKey'],
    )

    data = result.to_dict()

    assert data['signature'] == message['signature']
    assert data['public_key'] == message['publicKey']
    assert data['message'] == message['message']

def test_to_json(message):
    result = Message(
        message=message['message'],
        signature=message['signature'],
        public_key=message['publicKey'],
    )

    json_data = result.to_json()
    data = json.loads(json_data)

    assert data['signature'] == message['signature']
    assert data['public_key'] == message['publicKey']
    assert data['message'] == message['message']
