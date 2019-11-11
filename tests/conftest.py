import pytest


@pytest.fixture
def transaction_type_0():
    """Transaction of type "transfer"
    """
    data = {
        'version': 2,
        'network': 23,
        'typeGroup': 1,
        'type': 0,
        'nonce': 0,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 10000000,
        'amount': 200000000,
        'expiration': 0,
        'recipientId': 'AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC',
        'signature': '24cb51a214057e4af4fd80cf3a96374c9c16ee1bcd7110684b5995eed1f19a49e08bf032feba18475cf888116826a03fc50c3cf52a7456e7e5085db1191b4568',  # noqa
        'id': '7258453b1516ecf8be87e9aa0a3d00823197d1504ff76779e28743b4c8b5617c',
        'serialized': 'ff02170100000000000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19280969800000000000000c2eb0b0000000000000000170995750207ecaf0ccf251c1265b92ad84f55366224cb51a214057e4af4fd80cf3a96374c9c16ee1bcd7110684b5995eed1f19a49e08bf032feba18475cf888116826a03fc50c3cf52a7456e7e5085db1191b4568'  # noqa
    }
    return data


@pytest.fixture
def transaction_type_1():
    """Transaction of type "second signature registration"
    """
    data = {
        'version': 2,
        'network': 23,
        'typeGroup': 1,
        'type': 1,
        'nonce': 0,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 500000000,
        'asset': {
            'signature': {
                'publicKey': '03699e966b2525f9088a6941d8d94f7869964a000efe65783d78ac82e1199fe609'
            }
        },
        'signature': '60901885e7a4915fae19bbbd4d189fb1dd199d37650dfa6d6aea4495b5d0f28c674e83c4e198a1d2e789739c5523772c5dcf27d89a281868f8757801df89d848',  # noqa
        'amount': 0,
        'id': 'd1e5513ee2c13994dbd4a9fc134740b25e222d1737816c6a48a69cf6ca209a4b',
        'serialized': 'ff02170100000001000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1920065cd1d000000000003699e966b2525f9088a6941d8d94f7869964a000efe65783d78ac82e1199fe60960901885e7a4915fae19bbbd4d189fb1dd199d37650dfa6d6aea4495b5d0f28c674e83c4e198a1d2e789739c5523772c5dcf27d89a281868f8757801df89d848'  # noqa
    }
    return data


@pytest.fixture
def transaction_type_2():
    """Transaction of type "delegate registration"
    """
    data = {
        'version': 2,
        'network': 23,
        'typeGroup': 1,
        'type': 2,
        'nonce': 0,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 2500000000,
        'asset': {
            'delegate': {
                'username': 'boldninja'
            }
        },
        'signature': '5873d5eb98dbb1fe115cba4b0446d1e0f811b4e4cc3d5720dbbb234e12c9e65df41c0933a77394550cab0fb3e46dd70a102b14cf3f3032548b1dd50f6bc70458',  # noqa
        'amount': 0,
        'id': '994b3846637b97812fa1ff77fa3c2825d8c9ac9e895687806cb89cb09df27ad1',
        'serialized': 'ff02170100000002000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200f90295000000000009626f6c646e696e6a615873d5eb98dbb1fe115cba4b0446d1e0f811b4e4cc3d5720dbbb234e12c9e65df41c0933a77394550cab0fb3e46dd70a102b14cf3f3032548b1dd50f6bc70458'  # noqa
    }
    return data


@pytest.fixture
def transaction_type_3():
    """Transaction of type "vote"
    """
    data = {
        'version': 2,
        'network': 23,
        'typeGroup': 1,
        'type': 3,
        'nonce': 0,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 100000000,
        'asset': {
            'votes': ['+022cca9529ec97a772156c152a00aad155ee6708243e65c9d211a589cb5d43234d']
        },
        'signature': '35f778a736ad80233e478df16d7a628e205915c35031ec3a99a74f8b078ec951bdb5df32f44dde9518338d5174008326605bb4561a26fc0ca57b9c2163dfa91b',  # noqa
        'amount': 0,
        'id': 'a83f69bc0111692757be9e7d1eabb582e8a67b7357ff92063fc37fe72d605865',
        'serialized': 'ff02170100000003000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200e1f50500000000000101022cca9529ec97a772156c152a00aad155ee6708243e65c9d211a589cb5d43234d35f778a736ad80233e478df16d7a628e205915c35031ec3a99a74f8b078ec951bdb5df32f44dde9518338d5174008326605bb4561a26fc0ca57b9c2163dfa91b'  # noqa
    }
    return data


@pytest.fixture
def transaction_type_4():
    """Transaction of type "multi signature registration"
    """
    data = {
        'version': 2,
        'network': 23,
        'typeGroup': 1,
        'type': 4,
        'nonce': 0,
        'senderPublicKey': '0205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b896',
        'id': '4e3ad8fdf95cdcc871ca09be64626059759e094ce7feed1acd794e69777dc472',
        'blockid': '1844069042066945391',
        'amount': 0,
        'fee': 2000000000,
        'signature': '3b316d16f8fe2ed58abf46379126be1978f222092085d5bf3c887f6c5329956c4b1141611e57682362c0962bcadd2d68d368904aff2a4443d0e4039c984fb23c',  # noqa
        'signSignature': '304402201fcd54a9ac9c0269b8cec213566ddf43207798e2cf9ca1ce3c5d315d66321c6902201aa94c4ed3e5e479a12220aa886b259e488eb89b697c711f91e8c03b9620e0b1',  # noqa
        'signatures': [
            '0088049c54917fd5319a33668d419efb87e9c90c274651614d89d4c5db5590b90417e7d7babb17ff49cc787e21f527757261a2d94df256606eab9f4e3b0221459b',  # noqa
            '01ed57f6bdd7524cd54961d446a86552a6adcae892fcff3e1c9bae12f4c0c80f85e04a3826c992fafbbbbaa3261b72587743f3aaf21ed7dd1c3af04ffe9b3f4afb',  # noqa
            '02a9518f8e314dc880d359367c77c7ec5c45c3f7c9cad129da439e2a2f3e1421adbac65f17c4615bd12fdbe9bad0856dbbdec12531d82fd0297f16b11c436c54ee'  # noqa
        ],
        'asset': {
            'multiSignature': {
                'min': 2,
                'publicKeys': [
                    '0205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b896',
                    '03df0a1eb42d99b5de395cead145ba1ec2ea837be308c7ce3a4e8018b7efc7fdb8',
                    '03860d76b1df09659ac282cea3da5bd84fc45729f348a4a8e5f802186be72dc17f'
                ],
            }
        },
        'serialized': 'ff021701000000040000000000000000000205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b89600943577000000000002030205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b89603df0a1eb42d99b5de395cead145ba1ec2ea837be308c7ce3a4e8018b7efc7fdb803860d76b1df09659ac282cea3da5bd84fc45729f348a4a8e5f802186be72dc17f3b316d16f8fe2ed58abf46379126be1978f222092085d5bf3c887f6c5329956c4b1141611e57682362c0962bcadd2d68d368904aff2a4443d0e4039c984fb23c0088049c54917fd5319a33668d419efb87e9c90c274651614d89d4c5db5590b90417e7d7babb17ff49cc787e21f527757261a2d94df256606eab9f4e3b0221459b01ed57f6bdd7524cd54961d446a86552a6adcae892fcff3e1c9bae12f4c0c80f85e04a3826c992fafbbbbaa3261b72587743f3aaf21ed7dd1c3af04ffe9b3f4afb02a9518f8e314dc880d359367c77c7ec5c45c3f7c9cad129da439e2a2f3e1421adbac65f17c4615bd12fdbe9bad0856dbbdec12531d82fd0297f16b11c436c54ee'  # noqa
    }
    return data


@pytest.fixture
def transaction_type_5():
    """Transaction of type "ipfs"
    """
    data = {
        'version': 2,
        'network': 23,
        'typeGroup': 1,
        'type': 5,
        'nonce': 0,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 500000000,
        'amount': 0,
        'asset': {
            'ipfs': 'QmR45FmbVVrixReBwJkhEKde2qwHYaQzGxu4ZoDeswuF9w'
        },
        'signature': '13109c588e5e2646756f13f4e73f8c0791c0ddf3508fbb34373c38817ce81e8c57ee09915fa5fd63487749ad91da2544795e0d8a1d1722a2fbfb94a58469c8fd',
        'id': '3959056991f3b56ea767dc63fad1b3bc135572bf03dd7ac339aeaff445fa7193',
        'serialized': 'ff02170100000005000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1920065cd1d000000000012202853f0f11ab91d73b73a2a86606103f45dd469ad2e89ec6f9a25febe8758d3fe13109c588e5e2646756f13f4e73f8c0791c0ddf3508fbb34373c38817ce81e8c57ee09915fa5fd63487749ad91da2544795e0d8a1d1722a2fbfb94a58469c8fd'
    }
    return data


@pytest.fixture
def transaction_type_6():
    """Transaction of type "multi payment"
    """
    data = {
        'version': 2,
        'network': 23,
        'typeGroup': 1,
        'type': 6,
        'nonce': 0,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 10000000,
        'amount': 0,
        'asset': {
            'payments': [
                {
                    'amount': 1,
                    'recipientId': 'AHXtmB84sTZ9Zd35h9Y1vfFvPE2Xzqj8ri'
                },
                {
                    'amount': 2,
                    'recipientId': 'AZFEPTWnn2Sn8wDZgCRF8ohwKkrmk2AZi1'
                },
            ],
        },
        'signature': '4d117d98368a63af5621a6608022bbbb3f14555f0afb3fbe807476e91f619cc9079c29b3267ca09f18283fa6b49feb9902e92cc3e5cf7dafc99c5f91d7d5fce7',
        'id': '466cf307cb286012356b248fa714698d0f567ef1a319c2048c9b1aa71251aae5',
        'serialized': 'ff02170100000006000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1928096980000000000000200010000000000000017134b5be4b327ddf9c2bb47fec8a1a44189e90f74020000000000000017bfa6aec83cf1bd03a0cab9f35c85ff51a3e9f0414d117d98368a63af5621a6608022bbbb3f14555f0afb3fbe807476e91f619cc9079c29b3267ca09f18283fa6b49feb9902e92cc3e5cf7dafc99c5f91d7d5fce7'
    }
    return data


@pytest.fixture
def transaction_type_7():
    """Transaction of type "delegate resignation"
    """
    data = {
        'version': 2,
        'network': 23,
        'typeGroup': 1,
        'type': 7,
        'nonce': 0,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 2500000000,
        'amount': 0,
        'signature': '0662fc939dbc79527786f4bfae360589d525e5c4e84bc0822eeccf9265601486445633813783ed166b37101b8faf595592557b75f84c842bc01221d64960c0e7',
        'id': '4f037d4d995d4ed950ad693aaccb72024f40ed8446d351df4c0deb9be1ae33ca',
        'serialized': 'ff02170100000007000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200f9029500000000000662fc939dbc79527786f4bfae360589d525e5c4e84bc0822eeccf9265601486445633813783ed166b37101b8faf595592557b75f84c842bc01221d64960c0e7'
    }
    return data


@pytest.fixture
def transaction_type_8():
    """Transaction of type "timelock transfer"
    """
    data = {
        'version': 2,
        'network': 23,
        'typeGroup': 1,
        'type': 8,
        'nonce': 0,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 10000000,
        'amount': 200000000,
        'vendorFieldHex': '74686973206973206120746f70207365637265742076656e646f72206669656c64',
        'vendorFied': 'this is a top secret vendor field',
        'recipientId': 'AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC',
        'asset': {
            'lock': {
                'secretHash': '0f128d401958b1b30ad0d10406f47f9489321017b4614e6cb993fc63913c5454',
                'expiration': {
                    'type': 1,
                    'value': 1573213026
                }
            },
        },
        'signature': 'e9d69dbdd03562886b1934968ac25e90b81d32a19c2e1ed3650568534afdb30e130dbaf18d1014edae1c8fe6f35b713e45fae48e9efeb201c63c4330d08bd413',
        'id': '9a51b6e77105adc793f3ae0619185f7730e63cd2af3fd823921bd35ee75dcab6',
        'serialized': 'ff02170100000008000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19280969800000000002174686973206973206120746f70207365637265742076656e646f72206669656c6400c2eb0b000000000f128d401958b1b30ad0d10406f47f9489321017b4614e6cb993fc63913c5454016253c55d170995750207ecaf0ccf251c1265b92ad84f553662e9d69dbdd03562886b1934968ac25e90b81d32a19c2e1ed3650568534afdb30e130dbaf18d1014edae1c8fe6f35b713e45fae48e9efeb201c63c4330d08bd413'

    }
    return data

@pytest.fixture
def transaction_type_9():
    """Transaction of type "timelock claim"
    """
    data = {
        'version': 2,
        'network': 23,
        'typeGroup': 1,
        'type': 9,
        'nonce': 0,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 0,
        'amount': 0,
        'asset': {
            'claim': {
                'lockTransactionId': '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4',
                'unlockSecret': 'my secret that should be 32bytes'
            },
        },
        'signature': 'acd0309b622a5163237748e046cc07eb66006a7fad5fde7d37f8a291fcf70b81dce12c4d473ab5f0d81fe9c1862f9287fae2b019b852f8931fd475bfbc04973c',
        'id': '4a7e5567d88f71bc3a0561696f7f1e1f9464dbd231f0ba18d25720be80bf699e',
        'serialised': 'ff02170100000009000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192000000000000000000943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb46d792073656372657420746861742073686f756c642062652033326279746573acd0309b622a5163237748e046cc07eb66006a7fad5fde7d37f8a291fcf70b81dce12c4d473ab5f0d81fe9c1862f9287fae2b019b852f8931fd475bfbc04973c'

    }
    return data

@pytest.fixture
def transaction_type_10():
    """Transaction of type "timelock refund"
    """
    data = {
        'version': 2,
        'network': 23,
        'typeGroup': 1,
        'type': 10,
        'nonce': 0,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 0,
        'amount': 0,
        'asset': {
            'refund': {
                'lockTransactionId': '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4',
            },
        },
        'signature': 'be99fb012a892fb56c25b413c4e3252c67bda9dfc73d3b5c6d6c7d811e6caa76a5bc2ff7f0a1e6faefeb501820b99985cd965411ab2156015d18493fec30b14c',
        'id': 'c55190242435657bf60804f76087dc42692f3ba1ef802e167096a30c9135428a',
        'serialized': 'ff0217010000000a000000000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192000000000000000000943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4be99fb012a892fb56c25b413c4e3252c67bda9dfc73d3b5c6d6c7d811e6caa76a5bc2ff7f0a1e6faefeb501820b99985cd965411ab2156015d18493fec30b14c'

    }
    return data


@pytest.fixture
def message():
    data = {
        'data': {
            'public_key': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
            'signature': '304402200fb4adddd1f1d652b544ea6ab62828a0a65b712ed447e2538db0caebfa68929e02205ecb2e1c63b29879c2ecf1255db506d671c8b3fa6017f67cfd1bf07e6edd1cc8',  # noqa
            'message': 'Hello World'
        },
        'passphrase': 'this is a top secret passphrase'
    }
    return data
