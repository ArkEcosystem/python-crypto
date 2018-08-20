from crypto.conf import use_network
from crypto.identity.address import (
    address_from_passphrase, address_from_private_key, address_from_public_key, validate_address
)


def test_address_from_public_key(identity):
    use_network('devnet')
    address = address_from_public_key(identity['data']['public_key'])
    assert address == identity['data']['address']


def test_address_from_private_key(identity):
    use_network('devnet')
    address = address_from_private_key(identity['data']['private_key'])
    assert address == identity['data']['address']


def test_address_from_passphrase(identity):
    use_network('devnet')
    address = address_from_passphrase(identity['passphrase'])
    assert address == identity['data']['address']


def test_validate_address(identity):
    use_network('devnet')
    assert validate_address(identity['data']['address']) is True
