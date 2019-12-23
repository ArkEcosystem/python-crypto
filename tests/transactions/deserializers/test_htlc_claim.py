from crypto.transactions.deserializer import Deserializer


def test_htlc_claim_deserializer():
    serialized = 'ff02170100000009000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192000000000000000000943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb46d792073656372657420746861742073686f756c642062652033326279746573381188e6a3c0da8823ab37cf7562724b3920f4fc8a40cb259ae297bd7237b511cbfdbcb46b7afa319ad1c2d8cc3d8cdc33a437c8b17867777b891d03c036dfb9'  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 2
    assert actual.network == 23
    assert actual.typeGroup == 1
    assert actual.type == 9
    assert actual.nonce == 1
    assert actual.senderPublicKey == '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192'
    assert actual.fee == 0
    assert actual.signature == '381188e6a3c0da8823ab37cf7562724b3920f4fc8a40cb259ae297bd7237b511cbfdbcb46b7afa319ad1c2d8cc3d8cdc33a437c8b17867777b891d03c036dfb9'
    assert actual.amount == 0
    assert actual.id == '846c5ee8a328376416735da43056d154d41e264564def42fb28b373c0d895c46'
    assert actual.asset['claim']['lockTransactionId'] == '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'  # noqa
    assert actual.asset['claim']['unlockSecret'] == 'my secret that should be 32bytes'  # noqa

    actual.verify_schnorr()
