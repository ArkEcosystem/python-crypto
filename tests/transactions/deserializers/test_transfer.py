from crypto.transactions.deserializer import Deserializer


def test_transfer_deserializer(transaction_type_0):
    deserializer = Deserializer(transaction_type_0['serialized'])
    actual = deserializer.deserialize()

    assert actual.version == transaction_type_0['version']
    assert actual.network == transaction_type_0['network']
    assert actual.typeGroup == transaction_type_0['typeGroup']
    assert actual.type == transaction_type_0['type']
    assert actual.nonce == transaction_type_0['nonce']
    assert actual.senderPublicKey == transaction_type_0['senderPublicKey']
    assert actual.fee == transaction_type_0['fee']
    assert actual.amount == transaction_type_0['amount']
    assert actual.expiration == transaction_type_0['expiration']
    assert actual.recipientId == transaction_type_0['recipientId']
    assert actual.signature == transaction_type_0['signature']
    assert actual.id == transaction_type_0['id']

    actual.verify_schnorr()
