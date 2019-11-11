from crypto.transactions.deserializer import Deserializer


def test_timelock_refund_deserializer():
    serialized = 'ff0217010000000a000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192000000000000000000943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4be99fb012a892fb56c25b413c4e3252c67bda9dfc73d3b5c6d6c7d811e6caa76a5bc2ff7f0a1e6faefeb501820b99985cd965411ab2156015d18493fec30b14c'  # noqa
    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    assert actual.asset['refund']['secretHalockTransactionIdsh'] == '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'  # noqa
    actual.verify()
