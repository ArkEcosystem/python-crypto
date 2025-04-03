from crypto.identity.address import Address

def test_address_from_public_key(identity):
    address = Address.from_public_key(identity['data']['public_key'])
    assert address == identity['data']['address']


def test_address_from_private_key(identity):
    address = Address.from_private_key(identity['data']['private_key'])
    assert address == identity['data']['address']


def test_address_from_passphrase(identity):
    address = Address.from_passphrase(identity['passphrase'])
    assert address == identity['data']['address']
