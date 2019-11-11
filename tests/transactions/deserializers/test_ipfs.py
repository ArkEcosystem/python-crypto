from crypto.transactions.deserializer import Deserializer


def test_ipfs_deserializer():
    serialized = 'ff02170100000005000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1920065cd1d000000000012202853f0f11ab91d73b73a2a86606103f45dd469ad2e89ec6f9a25febe8758d3fe13109c588e5e2646756f13f4e73f8c0791c0ddf3508fbb34373c38817ce81e8c57ee09915fa5fd63487749ad91da2544795e0d8a1d1722a2fbfb94a58469c8fd'  # noqa
    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    assert actual.asset['ipfs'] == 'QmR45FmbVVrixReBwJkhEKde2qwHYaQzGxu4ZoDeswuF9w'  # noqa
    # actual.verify()
