import json

from crypto.utils.message import Message


def test_signing(message):
    result = Message.sign(message['data']['message'], message['passphrase'])
    assert result.to_dict() == message['data']


def test_verify(message):
    result = Message(**message['data'])
    assert result.verify() is True

def test_to_dict(message):
    result = Message(**message['data'])
    assert result.to_dict() == message['data']


def test_to_json(message):
    result = Message(**message['data'])
    json_data = result.to_json()
    data = json.loads(json_data)
    assert data['signature'] == message['data']['signature']
    assert data['public_key'] == message['data']['public_key']
    assert data['message'] == message['data']['message']