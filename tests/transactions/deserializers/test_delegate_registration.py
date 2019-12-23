from crypto.transactions.deserializer import Deserializer


def test_delegate_registration_deserializer():
    serialized = 'ff02170100000002000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200f90295000000000009626f6c646e696e6a61eaf4b4dfd7903c32cf6c145ddf0744e86536719f5790b4286b08f1a10f0ad183bc601efc8a49a2a7b41758601a1793693afa1781cf0a63a8f72b08d5a1aaba1e'  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 2
    assert actual.network == 23
    assert actual.typeGroup == 1
    assert actual.type == 2
    assert actual.nonce == 1
    assert actual.senderPublicKey == '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192'
    assert actual.fee == 2500000000
    assert actual.asset['delegate'] == {'username': 'boldninja'}
    assert actual.signature == 'eaf4b4dfd7903c32cf6c145ddf0744e86536719f5790b4286b08f1a10f0ad183bc601efc8a49a2a7b41758601a1793693afa1781cf0a63a8f72b08d5a1aaba1e'
    assert actual.amount == 0
    assert actual.id == 'cfd113d8cd9fd46b07030c14fac38c1d3fc0eca991e999eab9d0152ea96ab0dc'

    actual.verify_schnorr()
