from crypto.transactions.deserializer import Deserializer


def test_htlc_claim_deserializer():
    serialized = 'ff021e0100000009000100000000000000037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c000000000000000000943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb46434323233626639336532303235303561366135303134323161383864396661dcd867411d20c7aa891e44cd92e916ea1d1e64ef1518dfcdfa227e4415d846a66c60718dc9d4bfc354afa69c2f8fa6e68f57e6eaf53c51b7a209ead5702ffd71'  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 2
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 9
    assert actual.nonce == 1
    assert actual.senderPublicKey == '037fde73baaa48eb75c013fe9ff52a74a096d48b9978351bdcb5b72331ca37487c'
    assert actual.fee == 0
    assert actual.signature == 'dcd867411d20c7aa891e44cd92e916ea1d1e64ef1518dfcdfa227e4415d846a66c60718dc9d4bfc354afa69c2f8fa6e68f57e6eaf53c51b7a209ead5702ffd71'
    assert actual.amount == 0
    assert actual.id == 'aad3fdb321e2543af1dd9d2d4d155473a8b49cacbc116fa1f3f1b95154b336d5'
    assert actual.asset['claim']['lockTransactionId'] == '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'  # noqa
    assert actual.asset['claim']['unlockSecret'] == '6434323233626639336532303235303561366135303134323161383864396661'  # noqa

    actual.verify_schnorr()
