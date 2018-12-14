import json

from crypto.utils.message import Message


def test_signing(message):
    result = Message.sign(message['data']['message'], message['passphrase'])
    assert result.to_dict() == message['data']


def test_verify_with_publickey(message):
    result = Message(**message['pk'])
    assert result.verify() is True


def test_verify_with_publicKey(message):
    result = Message(**message['data'])
    assert result.verify() is True


def test_to_dict(message):
    result = Message(**message['data'])
    assert result.to_dict() == message['data']


def test_to_json_with_publicKey(message):
    result = Message(**message['data'])
    json_data = result.to_json()
    data = json.loads(json_data)
    assert data['signature'] == message['data']['signature']
    assert data['publicKey'] == message['data']['publicKey']
    assert data['message'] == message['data']['message']


def test_to_json_with_publickey(message):
    result = Message(**message['pk'])
    json_data = result.to_json()
    data = json.loads(json_data)
    assert data['signature'] == message['pk']['signature']
    assert data['publickey'] == message['pk']['publickey']
    assert data['message'] == message['pk']['message']
