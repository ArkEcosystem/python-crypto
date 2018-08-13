from crypto.conf import use_network
from crypto.identity.address import (
    address_from_public_key, address_from_passphrase, address_from_private_key
)


def test_address_from_public_key():
    use_network('devnet')
    public_key = '03bd4f16e39aaba5cba6a87b7498b08ce540f279be367e68ae96fb05dfabe203ad'.encode()
    address = address_from_public_key(public_key)
    assert address == 'DBi2HdDY8TqMCD2aFLVomEF92gzeDmEHmR'.encode()


def test_address_from_private_key():
    use_network('devnet')
    private_key = 'd8839c2432bfd0a67ef10a804ba991eabba19f154a3d707917681d45822a5712'.encode()
    address = address_from_private_key(private_key)
    assert address == 'D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib'.encode()


def test_address_from_passphrase():
    use_network('devnet')
    passphrase = 'this is a top secret passphrase'.encode()
    address = address_from_passphrase(passphrase)
    assert address == 'D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib'.encode()
