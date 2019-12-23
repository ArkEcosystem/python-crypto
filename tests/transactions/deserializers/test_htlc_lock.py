from crypto.transactions.deserializer import Deserializer


def test_htlc_lock_deserializer():
    serialized = 'ff02170100000008000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19280969800000000000000c2eb0b000000000f128d401958b1b30ad0d10406f47f9489321017b4614e6cb993fc63913c545401ce07c95d170995750207ecaf0ccf251c1265b92ad84f5536627fe939b22a1da166b6ea58e3964651236fb4e0739f9716dedf92986f37df71ea7993e9a97b4a1686c0ad08028dcae08b7cb4a54b8a4db57e72b839a611e86358'  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 2
    assert actual.network == 23
    assert actual.typeGroup == 1
    assert actual.type == 8
    assert actual.nonce == 1
    assert actual.senderPublicKey == '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192'
    assert actual.fee == 10000000
    assert actual.signature == '7fe939b22a1da166b6ea58e3964651236fb4e0739f9716dedf92986f37df71ea7993e9a97b4a1686c0ad08028dcae08b7cb4a54b8a4db57e72b839a611e86358'
    assert actual.amount == 200000000
    assert actual.id == 'e1b34afa54bbf34de5c00716b92246c5248c2135221ece169db877ca60a14007'
    assert actual.recipientId == 'AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC'
    assert actual.asset['lock']['secretHash'] == '0f128d401958b1b30ad0d10406f47f9489321017b4614e6cb993fc63913c5454'  # noqa
    assert actual.asset['lock']['expiration']['type'] == 1  # noqa
    assert actual.asset['lock']['expiration']['value'] == 1573455822  # noqa

    actual.verify_schnorr()
