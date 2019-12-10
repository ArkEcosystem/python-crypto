from crypto.transactions.deserializer import Deserializer


def test_delegate_resignation_deserializer():
    serialized = 'ff02170100000007000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200f902950000000000bdc048ca7eb5688cc01921aecf5914118cfc78eacc23825efa6d75094a683127cc02512dc59e1e0631fa8956f482eabc54933d23011a8337ea9cab99abed504d'  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 2
    assert actual.network == 23
    assert actual.typeGroup == 1
    assert actual.type == 7
    assert actual.nonce == 1
    assert actual.senderPublicKey == '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192'
    assert actual.fee == 2500000000
    assert actual.signature == 'bdc048ca7eb5688cc01921aecf5914118cfc78eacc23825efa6d75094a683127cc02512dc59e1e0631fa8956f482eabc54933d23011a8337ea9cab99abed504d'
    assert actual.amount == 0
    assert actual.id == '707b4deb339e717dfef44c40db0692015ce9bbab015c007b016b8a46b341e859'

    actual.verify_schnorr()
