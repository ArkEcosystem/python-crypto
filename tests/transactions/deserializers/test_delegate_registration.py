from crypto.transactions.deserializer import Deserializer


def test_delegate_registration_deserializer():
    serialized = 'ff02170100000002000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200f90295000000000009626f6c646e696e6a61eaf4b4dfd7903c32cf6c145ddf0744e86536719f5790b4286b08f1a10f0ad183bc601efc8a49a2a7b41758601a1793693afa1781cf0a63a8f72b08d5a1aaba1e'  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.asset['delegate'] == {'username': 'boldninja'}

    # actual.verify()
