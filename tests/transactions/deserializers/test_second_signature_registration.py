from crypto.transactions.deserializer import Deserializer


def test_second_signature_registration_deserializer():
    serialized = 'ff02170100000001000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1920065cd1d000000000003699e966b2525f9088a6941d8d94f7869964a000efe65783d78ac82e1199fe609f9a1e2244c8318e8be85482fc02659e5c1775d246d73d5d0699ae4a1d5e3a3e84f9dcf68ee015f943d2a82eb829f35abd7901279761d96f6b43431520e955c67'  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 2
    assert actual.network == 23
    assert actual.typeGroup == 1
    assert actual.type == 1
    assert actual.nonce == 1
    assert actual.senderPublicKey == '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192'
    assert actual.fee == 500000000
    assert actual.signature == 'f9a1e2244c8318e8be85482fc02659e5c1775d246d73d5d0699ae4a1d5e3a3e84f9dcf68ee015f943d2a82eb829f35abd7901279761d96f6b43431520e955c67'
    assert actual.amount == 0
    assert actual.id == '173a3230159b45d772b2e0348f42af53913bf3e376397f29b8e0bda290badbe4'
    assert actual.asset['signature']['publicKey'] == '03699e966b2525f9088a6941d8d94f7869964a000efe65783d78ac82e1199fe609'  # noqa

    actual.verify_schnorr()
