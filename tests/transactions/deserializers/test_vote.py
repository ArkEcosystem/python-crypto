from crypto.transactions.deserializer import Deserializer


def test_vote_deserializer():
    serialized = 'ff02170100000003000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200e1f50500000000000101022cca9529ec97a772156c152a00aad155ee6708243e65c9d211a589cb5d43234d35f778a736ad80233e478df16d7a628e205915c35031ec3a99a74f8b078ec951bdb5df32f44dde9518338d5174008326605bb4561a26fc0ca57b9c2163dfa91b'  # noqa
    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    assert actual.asset['votes'] == ['+022cca9529ec97a772156c152a00aad155ee6708243e65c9d211a589cb5d43234d']  # noqa
    actual.verify()
