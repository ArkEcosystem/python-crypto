import json

from crypto.utils.message import Message


def test_signing(message):
    result = Message.sign(message['camelCase_pk']['message'], message['passphrase'])
    assert result.to_dict() == message['camelCase_pk']


def test_verify_with_publickey(message):
    result = Message(**message['snake_case_pk'])
    assert result.verify() is True


def test_verify_with_publicKey(message):
    result = Message(**message['camelCase_pk'])
    assert result.verify() is True


def test_to_dict(message):
    result = Message(**message['camelCase_pk'])
    assert result.to_dict() == message['camelCase_pk']


def test_to_json(message):
    result = Message(**message['camelCase_pk'])
    json_data = result.to_json()
    data = json.loads(json_data)
    assert data['signature'] == message['camelCase_pk']['signature']
    assert data['publicKey'] == message['camelCase_pk']['publicKey']
    assert data['message'] == message['camelCase_pk']['message']
