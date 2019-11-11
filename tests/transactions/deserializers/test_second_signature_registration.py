from crypto.transactions.deserializer import Deserializer


def test_second_signature_registration_deserializer():
    serialized = 'ff02170100000001000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1920065cd1d000000000003699e966b2525f9088a6941d8d94f7869964a000efe65783d78ac82e1199fe60960901885e7a4915fae19bbbd4d189fb1dd199d37650dfa6d6aea4495b5d0f28c674e83c4e198a1d2e789739c5523772c5dcf27d89a281868f8757801df89d848'  # noqa
    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    assert actual.asset['signature']['publicKey'] == '03699e966b2525f9088a6941d8d94f7869964a000efe65783d78ac82e1199fe609'  # noqa
    actual.verify()
