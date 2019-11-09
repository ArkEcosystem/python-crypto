from crypto.transactions.deserializer import Deserializer
from binascii import unhexlify, hexlify

def test_transfer_deserializer():
    serialized = 'ff02170100000000000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19280969800000000000000c2eb0b0000000000000000170995750207ecaf0ccf251c1265b92ad84f55366224cb51a214057e4af4fd80cf3a96374c9c16ee1bcd7110684b5995eed1f19a49e08bf032feba18475cf888116826a03fc50c3cf52a7456e7e5085db1191b4568'  # noqa
    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    assert actual.expiration == 0
    assert actual.type == 0
    assert actual.amount == 200000000
    assert actual.fee == 10000000
    assert actual.nonce == 0
    assert actual.recipientId == 'AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC'
    assert actual.senderPublicKey == '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192'  # noqa
    assert actual.id == '7258453b1516ecf8be87e9aa0a3d00823197d1504ff76779e28743b4c8b5617c'
    actual.verify()