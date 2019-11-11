from crypto.transactions.deserializer import Deserializer


def test_timelock_claim_deserializer():
    serialized = 'ff02170100000009000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192000000000000000000943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb46d792073656372657420746861742073686f756c642062652033326279746573acd0309b622a5163237748e046cc07eb66006a7fad5fde7d37f8a291fcf70b81dce12c4d473ab5f0d81fe9c1862f9287fae2b019b852f8931fd475bfbc04973c'  # noqa
    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    assert actual.asset['claim']['lockTransactionId'] == '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'  # noqa
    actual.verify()
