from crypto.transactions.deserializer import Deserializer


def test_multi_payment_deserializer():
    serialized = 'ff02170100000006000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1928096980000000000000200010000000000000017134b5be4b327ddf9c2bb47fec8a1a44189e90f74020000000000000017bfa6aec83cf1bd03a0cab9f35c85ff51a3e9f041672e89e66a9c5d7d95c21ccd07a89a111f02823146c06f14689d2cf1efd645fb648258fcf2280486d2cae19f391796d72145d2a8e6f261e887e34cd1998bdb65'  # noqa

    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()

    assert actual.version == 2
    assert actual.network == 23
    assert actual.typeGroup == 1
    assert actual.type == 6
    assert actual.nonce == 1
    assert actual.senderPublicKey == '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192'
    assert actual.fee == 10000000
    assert actual.signature == '672e89e66a9c5d7d95c21ccd07a89a111f02823146c06f14689d2cf1efd645fb648258fcf2280486d2cae19f391796d72145d2a8e6f261e887e34cd1998bdb65'
    assert actual.amount == 0
    assert actual.id == 'e8c7293d428048f8678dc6c88cb8b32bd49c8ae9b02018297c1889d9bd33ba8d'
    assert actual.asset['payments'][0]['amount'] == 1  # noqa
    assert actual.asset['payments'][0]['recipientId'] == 'AHXtmB84sTZ9Zd35h9Y1vfFvPE2Xzqj8ri'  # noqa
    assert actual.asset['payments'][1]['amount'] == 2  # noqa
    assert actual.asset['payments'][1]['recipientId'] == 'AZFEPTWnn2Sn8wDZgCRF8ohwKkrmk2AZi1'  # noqa

    actual.verify_schnorr()
