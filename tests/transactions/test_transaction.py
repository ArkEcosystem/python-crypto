from crypto.transactions.transaction import Transaction


def test_transaction_serialize(transaction_type_0):
    transaction = Transaction(**transaction_type_0)
    serialized = transaction.serialize(False, True, False)
    assert serialized == transaction_type_0['serialized']


def test_transaction_deserialize(transaction_type_0):
    transaction = Transaction()
    deserialized = transaction.deserialize(transaction_type_0['serialized'])
    data = deserialized.to_dict()
    assert data['amount'] == transaction_type_0['amount']
    assert data['senderPublicKey'] == transaction_type_0['senderPublicKey']
    assert data['recipientId'] == transaction_type_0['recipientId']
    assert data['id'] == transaction_type_0['id']
    assert data['fee'] == transaction_type_0['fee']
    assert data['signature'] == transaction_type_0['signature']
    assert data['version'] == transaction_type_0['version']
    assert data['network'] == transaction_type_0['network']
    assert data['type'] == transaction_type_0['type']
    assert data['typeGroup'] == transaction_type_0['typeGroup']
    assert data['nonce'] == transaction_type_0['nonce']
