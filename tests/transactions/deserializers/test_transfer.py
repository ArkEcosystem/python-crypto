from crypto.transactions.deserializer import Deserializer


def test_transfer_deserializer():
    serialized = 'ff011e0066b47502034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19280969800000000000000c2eb0b00000000000000001e0995750207ecaf0ccf251c1265b92ad84f5536623044022002994b30e08b58825c8c16ebf2cc693cfe706fb26571674784ead098accc89d702205b79dedc752a84504ecfe4b9e1292997f22260ee4daa102d2d9a61432d93b286'  # noqa
    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    assert actual.expiration == 0
    assert actual.type == 0
    assert actual.amount == 200000000
    assert actual.fee == 10000000
    assert actual.timestamp == 41268326
    assert actual.recipientId == 'D61mfSggzbvQgTUe6JhYKH2doHaqJ3Dyib'
    assert actual.senderPublicKey == '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192'  # noqa
    assert actual.id == 'da61c6cba363cc39baa0ca3f9ba2c5db81b9805045bd0b9fc58af07ad4206856'
    actual.verify()
