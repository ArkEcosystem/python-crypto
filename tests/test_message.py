import json
from collections import OrderedDict

from crypto.message import Message


def test_signing(message):
    result = Message.sign(message['data']['message'], message['passphrase'])
    assert OrderedDict(result.to_dict()) == OrderedDict(message['data'])


def test_verify(message):
    result = Message(**message['data'])
    assert result.verify() is True


def test_to_dict(message):
    result = Message(**message['data'])
    assert OrderedDict(result.to_dict()) == OrderedDict(message['data'])


def test_to_json(message):
    result = Message(**message['data'])
    json_data = result.to_json()
    assert OrderedDict(json.loads(json_data)) == OrderedDict(message['data'])
