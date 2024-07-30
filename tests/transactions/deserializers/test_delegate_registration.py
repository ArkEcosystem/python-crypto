from crypto.transactions.deserializer import Deserializer


def test_delegate_registration_deserializer(transaction_type_2):
    deserializer = Deserializer(transaction_type_2['serialized'])
    actual = deserializer.deserialize()

    assert actual.version == transaction_type_2['version']
    assert actual.network == transaction_type_2['network']
    assert actual.typeGroup == transaction_type_2['typeGroup']
    assert actual.type == transaction_type_2['type']
    assert actual.nonce == transaction_type_2['nonce']
    assert actual.senderPublicKey == transaction_type_2['senderPublicKey']
    assert actual.fee == transaction_type_2['fee']
    assert actual.asset == transaction_type_2['asset']
    assert actual.signature == transaction_type_2['signature']
    assert actual.amount == transaction_type_2['amount']
    assert actual.id == transaction_type_2['id']

    actual.verify_schnorr()
