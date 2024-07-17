from crypto.transactions.deserializer import Deserializer


def test_vote_deserializer():
    serialized = 'ff011e0100000003000100000000000000023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d300e1f50500000000000103f25455408f9a7e6c6a056b121e68fbda98f3511d22e9ef27b0ebaf1ef9e4eabc00b3b1e493a74187bb74416a58df503e35922ac1971e67d8380e991d46dc66ed50002f778c86a3d3353a2ab0749370ebd9d07f47022e3789cf73e2906c17990428'  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 1
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 3
    assert actual.amount == 0
    assert actual.fee == 100000000
    assert actual.nonce == 1
    assert actual.senderPublicKey == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'  # noqa
    assert actual.signature == 'b3b1e493a74187bb74416a58df503e35922ac1971e67d8380e991d46dc66ed50002f778c86a3d3353a2ab0749370ebd9d07f47022e3789cf73e2906c17990428'

    assert actual.asset['votes'] == ['+03f25455408f9a7e6c6a056b121e68fbda98f3511d22e9ef27b0ebaf1ef9e4eabc']  # noqa

    actual.verify_schnorr()
