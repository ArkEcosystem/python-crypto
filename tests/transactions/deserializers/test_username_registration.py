from crypto.transactions.deserializer import Deserializer


def test_username_registration_deserializer(transaction_type_8):
    deserializer = Deserializer(transaction_type_8['serialized'])
    actual = deserializer.deserialize()

    assert actual.version == transaction_type_8['version']
    assert actual.network == transaction_type_8['network']
    assert actual.typeGroup == transaction_type_8['typeGroup']
    assert actual.type == transaction_type_8['type']
    assert actual.nonce == transaction_type_8['nonce']
    assert actual.senderPublicKey == transaction_type_8['senderPublicKey']
    assert actual.fee == transaction_type_8['fee']
    assert actual.asset == transaction_type_8['asset']
    assert actual.signature == transaction_type_8['signature']
    assert actual.amount == transaction_type_8['amount']
    assert actual.id == transaction_type_8['id']

    actual.verify_schnorr()
