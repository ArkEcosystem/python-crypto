from crypto.transactions.deserializer import Deserializer


def test_multi_signature_registration_deserializer(transaction_type_4):
    deserializer = Deserializer(transaction_type_4['serialized'])
    actual = deserializer.deserialize()

    assert actual.version == transaction_type_4['version']
    assert actual.network == transaction_type_4['network']
    assert actual.typeGroup == transaction_type_4['typeGroup']
    assert actual.type == transaction_type_4['type']
    assert actual.nonce == transaction_type_4['nonce']
    assert actual.senderPublicKey == transaction_type_4['senderPublicKey']
    assert actual.fee == transaction_type_4['fee']
    assert actual.amount == transaction_type_4['amount']
    assert actual.signature == transaction_type_4['signature']
    assert actual.id == transaction_type_4['id']

    assert actual.asset['multiSignature']['min'] == transaction_type_4['asset']['multiSignature']['min']
    assert actual.asset['multiSignature']['publicKeys'] == transaction_type_4['asset']['multiSignature']['publicKeys']
    assert actual.signatures == transaction_type_4['signatures']

    actual.verify_multisig_schnorr()
