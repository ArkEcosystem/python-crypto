from crypto.transactions.deserializer import Deserializer


def test_delegate_registration_deserializer():
    serialized = 'ff02170100000002000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200f90295000000000009626f6c646e696e6a615873d5eb98dbb1fe115cba4b0446d1e0f811b4e4cc3d5720dbbb234e12c9e65df41c0933a77394550cab0fb3e46dd70a102b14cf3f3032548b1dd50f6bc70458'  # noqa
    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    assert actual.asset['delegate'] == {'username': 'boldninja'}
    # actual.verify()
