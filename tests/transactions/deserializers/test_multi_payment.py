from crypto.transactions.deserializer import Deserializer


def test_multi_payment_deserializer():
    serialized = 'ff02170100000006000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1928096980000000000000200010000000000000017134b5be4b327ddf9c2bb47fec8a1a44189e90f74020000000000000017bfa6aec83cf1bd03a0cab9f35c85ff51a3e9f0414d117d98368a63af5621a6608022bbbb3f14555f0afb3fbe807476e91f619cc9079c29b3267ca09f18283fa6b49feb9902e92cc3e5cf7dafc99c5f91d7d5fce7'  # noqa
    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    assert actual.asset['payments']['amount'] == 1  # noqa
    # actual.verify()
