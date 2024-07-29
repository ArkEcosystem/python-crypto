from crypto.transactions.deserializer import Deserializer


def test_multi_payment_deserializer():
    serialized = 'ff011e0100000006000500000000000000023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3809698000000000000020000e1f505000000006f0182a0cc707b055322ccf6d4cb6a5aff1aeb2200c2eb0b00000000b693449adda7efc015d87944eae8b7c37eb1690a6031b2c73de394a12b4988f43f0fe13cd7782469857914b92e6c05561ff6d7634783a89157e487dc38f104bf40fc279c38602dbfba0cc679dfe631ba4c77929c'  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 1
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 6
    assert actual.nonce == 5
    assert actual.senderPublicKey == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'
    assert actual.fee == 10000000
    assert actual.amount == 0
    assert actual.asset['payments'][0]['amount'] == 100000000  # noqa
    assert actual.asset['payments'][0]['recipientId'] == '0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22'  # noqa
    assert actual.asset['payments'][1]['amount'] == 200000000  # noqa
    assert actual.asset['payments'][1]['recipientId'] == '0xb693449AdDa7EFc015D87944EAE8b7C37EB1690A'  # noqa
    assert actual.signature == '6031b2c73de394a12b4988f43f0fe13cd7782469857914b92e6c05561ff6d7634783a89157e487dc38f104bf40fc279c38602dbfba0cc679dfe631ba4c77929c'
    assert actual.id == '46799c223ff8f19d00c3e3bd617c6692f3cab1aed33dbc99ad9706d22f709c5e'

    actual.verify_schnorr()
