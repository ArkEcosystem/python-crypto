import pytest
from crypto.identity.address import (
    address_from_passphrase, address_from_private_key, address_from_public_key
)

def test_address_from_public_key(identity):
    address = address_from_public_key(identity['data']['public_key'])
    assert address == identity['data']['address']


def test_address_from_private_key(identity):
    address = address_from_private_key(identity['data']['private_key'])
    assert address == identity['data']['address']


def test_address_from_passphrase(identity):
    address = address_from_passphrase(identity['passphrase'])
    assert address == identity['data']['address']
