from crypto.transactions.deserializer import Deserializer


def test_vote_deserializer():
    serialized = 'ff02170100000003000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200e1f50500000000000101022cca9529ec97a772156c152a00aad155ee6708243e65c9d211a589cb5d43234d86007f8e6a982bc271ec063c20f158734f0bc1e23e0e1abf9edeaa208b4810fa1d466171bba79a5c00b0a4c698728f68aa0748d98613cac247c014ee84a6fc41'  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 2
    assert actual.network == 23
    assert actual.typeGroup == 1
    assert actual.type == 3
    assert actual.amount == 0
    assert actual.fee == 100000000
    assert actual.nonce == 1
    assert actual.senderPublicKey == '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192'  # noqa
    assert actual.id == '2c5d71028607674411c8e37e316a015eccbeb9ba486fddfbd393dc421540a90a'
    assert actual.signature == '86007f8e6a982bc271ec063c20f158734f0bc1e23e0e1abf9edeaa208b4810fa1d466171bba79a5c00b0a4c698728f68aa0748d98613cac247c014ee84a6fc41'

    assert actual.asset['votes'] == ['+022cca9529ec97a772156c152a00aad155ee6708243e65c9d211a589cb5d43234d']  # noqa

    actual.verify_schnorr()
