from crypto.transactions.deserializer import Deserializer


def test_multi_payment_deserializer(transaction_type_6):
    deserializer = Deserializer(transaction_type_6['serialized'])
    actual = deserializer.deserialize()

    assert actual.version == transaction_type_6['version']
    assert actual.network == transaction_type_6['network']
    assert actual.typeGroup == transaction_type_6['typeGroup']
    assert actual.type == transaction_type_6['type']
    assert actual.nonce == transaction_type_6['nonce']
    assert actual.senderPublicKey == transaction_type_6['senderPublicKey']
    assert actual.fee == transaction_type_6['fee']
    assert actual.amount == transaction_type_6['amount']
    assert actual.signature == transaction_type_6['signature']
    assert actual.id == transaction_type_6['id']

    for index, payment in enumerate(transaction_type_6['asset']['payments']):
        assert actual.asset['payments'][index]['amount'] == payment['amount']
        assert actual.asset['payments'][index]['recipientId'] == payment['recipientId']

    actual.verify_schnorr()
