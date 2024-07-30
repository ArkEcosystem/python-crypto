from crypto.transactions.deserializer import Deserializer


def test_validator_resignation_deserializer(transaction_type_7):
    deserializer = Deserializer(transaction_type_7['serialized'])
    actual = deserializer.deserialize()

    assert actual.version == transaction_type_7['version']
    assert actual.network == transaction_type_7['network']
    assert actual.typeGroup == transaction_type_7['typeGroup']
    assert actual.type == transaction_type_7['type']
    assert actual.nonce == transaction_type_7['nonce']
    assert actual.senderPublicKey == transaction_type_7['senderPublicKey']
    assert actual.fee == transaction_type_7['fee']
    assert actual.signature == transaction_type_7['signature']
    assert actual.amount == transaction_type_7['amount']
    assert actual.id == transaction_type_7['id']

    actual.verify_schnorr()
