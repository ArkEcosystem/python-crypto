from crypto.transactions.deserializer import Deserializer


def test_vote_deserializer(transaction_type_3):
    deserializer = Deserializer(transaction_type_3['serialized'])
    actual = deserializer.deserialize()

    assert actual.version == transaction_type_3['version']
    assert actual.network == transaction_type_3['network']
    assert actual.typeGroup == transaction_type_3['typeGroup']
    assert actual.type == transaction_type_3['type']
    assert actual.amount == transaction_type_3['amount']
    assert actual.fee == transaction_type_3['fee']
    assert actual.nonce == transaction_type_3['nonce']
    assert actual.senderPublicKey == transaction_type_3['senderPublicKey']  # noqa
    assert actual.signature == transaction_type_3['signature']

    assert actual.asset == transaction_type_3['asset']  # noqa

    actual.verify_schnorr()
