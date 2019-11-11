from crypto.transactions.deserializer import Deserializer


def test_delegate_resignation_deserializer():
    serialized = 'ff02170100000007000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200f9029500000000000662fc939dbc79527786f4bfae360589d525e5c4e84bc0822eeccf9265601486445633813783ed166b37101b8faf595592557b75f84c842bc01221d64960c0e7'  # noqa
    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    assert actual.asset['type'] == 7
    #actual.verify()
