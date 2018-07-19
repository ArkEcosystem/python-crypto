from crypto.identity.keys import privat_key_from_passphrase, public_key_from_passphrase


def test_privat_key_from_passphrase():
    private_key = privat_key_from_passphrase('this is a top secret passphrase'.encode())
    assert private_key == b'd8839c2432bfd0a67ef10a804ba991eabba19f154a3d707917681d45822a5712'


def test_public_key_from_passphrase():
    public_key = public_key_from_passphrase('this is a top secret passphrase'.encode())
    assert public_key == b'034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192'
