from crypto.conf import use_network
from crypto.identity.wif import wif_from_passphrase


def test_wif_from_passphrase():
    use_network('devnet')
    result = wif_from_passphrase('this is a top secret passphrase'.encode())
    assert result == 'SGq4xLgZKCGxs7bjmwnBrWcT4C1ADFEermj846KC97FSv1WFD1dA'.encode()
