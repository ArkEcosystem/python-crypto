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


@pytest.mark.skip()
def test_transfer_second_signature_deserializer():
    serialized = 'ff02170100000000000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19280969800000000000000c2eb0b0000000000000000170995750207ecaf0ccf251c1265b92ad84f553662136c29d921b58ae3194020b82e9808f9cd54f7178cb34678f570f28226b8e56ba0ad318297a3bacbb37ab22ddaa5dbf1901cda3ec2d2bca5ce98d6407839ab9b02dd94f611e300ad77147d808a34e942b379c5468760d8605adc0304400a2578a2039468b844f30ad1f0515f9cce33855791296117bfe8ef3caa664152644fd6'

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 2
    assert actual.network == 23
    assert actual.typeGroup == 1
    assert actual.expiration == 0
    assert actual.type == 0
    assert actual.amount == 200000000
    assert actual.fee == 10000000
    assert actual.nonce == 1
    assert actual.recipientId == 'AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC'
    assert actual.senderPublicKey == '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192'  # noqa
    assert actual.id == 'be148ab83b75c199f9778f8963814a641a6ee937b6dd5b294082fbf7def94a45'
    assert actual.signature == '136c29d921b58ae3194020b82e9808f9cd54f7178cb34678f570f28226b8e56ba0ad318297a3bacbb37ab22ddaa5dbf1901cda3ec2d2bca5ce98d6407839ab9b'
    assert actual.signSignature == '02dd94f611e300ad77147d808a34e942b379c5468760d8605adc0304400a2578a2039468b844f30ad1f0515f9cce33855791296117bfe8ef3caa664152644fd6'

    actual.verify_schnorr()
