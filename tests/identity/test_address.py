from crypto.conf import use_network
from crypto.identity.address import address_from_public_key


def test_address_from_public_key():
    use_network('devnet')
    public_key = '03bd4f16e39aaba5cba6a87b7498b08ce540f279be367e68ae96fb05dfabe203ad'.encode()
    address = address_from_public_key(public_key)
    assert address == 'DBi2HdDY8TqMCD2aFLVomEF92gzeDmEHmR'.encode()
