from crypto.transactions.deserializer import Deserializer


def test_username_resignation_deserializer(transaction_type_9):
    deserializer = Deserializer(transaction_type_9['serialized'])
    actual = deserializer.deserialize()

    assert actual.version == transaction_type_9['version']
    assert actual.network == transaction_type_9['network']
    assert actual.typeGroup == transaction_type_9['typeGroup']
    assert actual.type == transaction_type_9['type']
    assert actual.nonce == transaction_type_9['nonce']
    assert actual.senderPublicKey == transaction_type_9['senderPublicKey']
    assert actual.fee == transaction_type_9['fee']
    assert actual.signature == transaction_type_9['signature']
    assert actual.amount == transaction_type_9['amount']
    assert actual.id == transaction_type_9['id']

    actual.verify_schnorr()
