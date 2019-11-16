from crypto.transactions.deserializer import Deserializer

def test_ipfs_deserializer():
    serialized = 'ff02170100000005000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1920065cd1d000000000012202853f0f11ab91d73b73a2a86606103f45dd469ad2e89ec6f9a25febe8758d3fe0b6e81b123de99e953d3073a8760d3213ab5f5cf512e65a2dd73aebb410966d8fbc59e775deb4f23c51be0847402b5e1d4ee68732b3e6d8e8914d259d7e373eb'  # noqa
    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    assert actual.asset['ipfs'] == 'QmR45FmbVVrixReBwJkhEKde2qwHYaQzGxu4ZoDeswuF9w'  # noqa
    # actual.verify()
