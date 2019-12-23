from crypto.transactions.deserializer import Deserializer


def test_htlc_refund_deserializer():
    serialized = 'ff0217010000000a000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192000000000000000000943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb416d9ef1dceb0cbb105a45af6bdde9439055f07197643f9e2837312463330fd02ec7b13d1242becfe333c1b8ab2ea91c0c8240390d86f0fb0f6cdc22ec6ac64f1'  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 2
    assert actual.network == 23
    assert actual.typeGroup == 1
    assert actual.type == 10
    assert actual.nonce == 1
    assert actual.senderPublicKey == '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192'
    assert actual.fee == 0
    assert actual.signature == '16d9ef1dceb0cbb105a45af6bdde9439055f07197643f9e2837312463330fd02ec7b13d1242becfe333c1b8ab2ea91c0c8240390d86f0fb0f6cdc22ec6ac64f1'
    assert actual.amount == 0
    assert actual.id == '9356aa730990a2ea8e9871ffa65800f34ef1a4bec3215d89c950e72d82a34e91'
    assert actual.asset['refund']['lockTransactionId'] == '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'  # noqa

    actual.verify_schnorr()
