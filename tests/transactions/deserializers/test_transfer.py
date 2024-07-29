import pytest
from crypto.transactions.deserializer import Deserializer


def test_transfer_deserializer():
    serialized = 'ff011e0100000000000300000000000000023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d38096980000000000000100000000000000000000006f0182a0cc707b055322ccf6d4cb6a5aff1aeb221c9e1c2493b1e597d682f31700989f76eec068375d4ce5e1721cc9265b66c9b551ea1afa28c4f443120e43cff5cc7f137c4572749b0467561038127b4eafded9'

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 1
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 0
    assert actual.nonce == 3
    assert actual.senderPublicKey == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'  # noqa
    assert actual.fee == 10000000
    assert actual.amount == 1
    assert actual.expiration == 0
    assert actual.recipientId == '0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22'
    assert actual.signature == '1c9e1c2493b1e597d682f31700989f76eec068375d4ce5e1721cc9265b66c9b551ea1afa28c4f443120e43cff5cc7f137c4572749b0467561038127b4eafded9'
    assert actual.id == '8d0584d1bbc8fa7a6e4e7904b884f69399df56dcfe6458c2bedc283c55604def'

    actual.verify_schnorr()
