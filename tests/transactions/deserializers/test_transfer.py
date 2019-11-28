from crypto.transactions.deserializer import Deserializer


def test_transfer_deserializer():
    serialized = 'ff02170100000000000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19280969800000000000000c2eb0b0000000000000000170995750207ecaf0ccf251c1265b92ad84f553662136c29d921b58ae3194020b82e9808f9cd54f7178cb34678f570f28226b8e56ba0ad318297a3bacbb37ab22ddaa5dbf1901cda3ec2d2bca5ce98d6407839ab9b'  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    print(actual.to_dict())

    assert actual.expiration == 0
    assert actual.type == 0
    assert actual.amount == 200000000
    assert actual.fee == 10000000
    assert actual.nonce == 1
    assert actual.network == 23
    assert actual.recipientId == 'AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC'
    assert actual.senderPublicKey == '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192'  # noqa
    assert actual.id == '129517023bd895b682bbb38b1d1f99e9222bd487899c843da22d8572b0fb52a8'

    #actual.verify()