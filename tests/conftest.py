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
        'nonce': 1,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 10000000,
        'amount': 200000000,
        'expiration': 0,
        'recipientId': 'AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC',
        'signature': '136c29d921b58ae3194020b82e9808f9cd54f7178cb34678f570f28226b8e56ba0ad318297a3bacbb37ab22ddaa5dbf1901cda3ec2d2bca5ce98d6407839ab9b',  # noqa
        'id': '129517023bd895b682bbb38b1d1f99e9222bd487899c843da22d8572b0fb52a8',
        'serialized': 'ff02170100000000000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19280969800000000000000c2eb0b0000000000000000170995750207ecaf0ccf251c1265b92ad84f553662136c29d921b58ae3194020b82e9808f9cd54f7178cb34678f570f28226b8e56ba0ad318297a3bacbb37ab22ddaa5dbf1901cda3ec2d2bca5ce98d6407839ab9b'  # noqa
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
        'nonce': 1,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 500000000,
        'asset': {
            'signature': {
                'publicKey': '03699e966b2525f9088a6941d8d94f7869964a000efe65783d78ac82e1199fe609'
            }
        },
        'signature': 'f9a1e2244c8318e8be85482fc02659e5c1775d246d73d5d0699ae4a1d5e3a3e84f9dcf68ee015f943d2a82eb829f35abd7901279761d96f6b43431520e955c67',  # noqa
        'amount': 0,
        'id': '173a3230159b45d772b2e0348f42af53913bf3e376397f29b8e0bda290badbe4',
        'serialized': 'ff02170100000001000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1920065cd1d000000000003699e966b2525f9088a6941d8d94f7869964a000efe65783d78ac82e1199fe609f9a1e2244c8318e8be85482fc02659e5c1775d246d73d5d0699ae4a1d5e3a3e84f9dcf68ee015f943d2a82eb829f35abd7901279761d96f6b43431520e955c67'  # noqa
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
        'nonce': 1,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 2500000000,
        'asset': {
            'delegate': {
                'username': 'boldninja'
            }
        },
        'signature': 'eaf4b4dfd7903c32cf6c145ddf0744e86536719f5790b4286b08f1a10f0ad183bc601efc8a49a2a7b41758601a1793693afa1781cf0a63a8f72b08d5a1aaba1e',  # noqa
        'amount': 0,
        'id': 'cfd113d8cd9fd46b07030c14fac38c1d3fc0eca991e999eab9d0152ea96ab0dc',
        'serialized': 'ff02170100000002000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200f90295000000000009626f6c646e696e6a61eaf4b4dfd7903c32cf6c145ddf0744e86536719f5790b4286b08f1a10f0ad183bc601efc8a49a2a7b41758601a1793693afa1781cf0a63a8f72b08d5a1aaba1e'  # noqa
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
        'nonce': 1,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 100000000,
        'asset': {
            'votes': ['+022cca9529ec97a772156c152a00aad155ee6708243e65c9d211a589cb5d43234d']
        },
        'signature': '86007f8e6a982bc271ec063c20f158734f0bc1e23e0e1abf9edeaa208b4810fa1d466171bba79a5c00b0a4c698728f68aa0748d98613cac247c014ee84a6fc41',  # noqa
        'amount': 0,
        'id': '2c5d71028607674411c8e37e316a015eccbeb9ba486fddfbd393dc421540a90a',
        'serialized': 'ff02170100000003000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200e1f50500000000000101022cca9529ec97a772156c152a00aad155ee6708243e65c9d211a589cb5d43234d86007f8e6a982bc271ec063c20f158734f0bc1e23e0e1abf9edeaa208b4810fa1d466171bba79a5c00b0a4c698728f68aa0748d98613cac247c014ee84a6fc41'  # noqa
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
        'nonce': 1,
        'senderPublicKey': '0205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b896',
        'id': 'c868aad20165a336c35e324378f0c12008d18af4c1025291efcb7539c7c917f0',
        'amount': 0,
        'fee': 2000000000,
        'signature': 'f5e9859c955bf8917b308ea21c88daf58661686c2017e476dcf735ad7f00aebf8e6effda3fe99e5f33f6007db7db9c9155796d9b5d31c53bd6156364a6a765d0',  # noqa
        'asset': {
            'multiSignature': {
                'publicKeys': [
                    '0205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b896',
                    '03df0a1eb42d99b5de395cead145ba1ec2ea837be308c7ce3a4e8018b7efc7fdb8',
                    '03860d76b1df09659ac282cea3da5bd84fc45729f348a4a8e5f802186be72dc17f'
                ],
                'min': 2,
            }
        },
        'signatures': [
            '0064900cb2cc3db6ca9c7e3bd363b322cdc4a39e051f655e9867935e1bb856b6dcce52845c031c690808f40340bc827bbaacd7b04bceff866cb0d386ab84715174',  # noqa
            '01dd363ccc101a958bded1a5db1c08f13283fc7cee53da93dfe00785eb406512467ff8e445f8ad843744ac4179f30f942645dfd5bdf5f2bfc344ad02393053880a',  # noqa
            '02d0012f035dc3fd54173c83d40217914653488fe9ce592dca34234163181d255281f2be7033725cfc4a6786509e7fabbaf0be8cf50882fc7b66fe94f259fd004e'  # noqa
        ],
        'serialized': 'ff021701000000040001000000000000000205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b89600943577000000000002030205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b89603df0a1eb42d99b5de395cead145ba1ec2ea837be308c7ce3a4e8018b7efc7fdb803860d76b1df09659ac282cea3da5bd84fc45729f348a4a8e5f802186be72dc17ff5e9859c955bf8917b308ea21c88daf58661686c2017e476dcf735ad7f00aebf8e6effda3fe99e5f33f6007db7db9c9155796d9b5d31c53bd6156364a6a765d00064900cb2cc3db6ca9c7e3bd363b322cdc4a39e051f655e9867935e1bb856b6dcce52845c031c690808f40340bc827bbaacd7b04bceff866cb0d386ab8471517401dd363ccc101a958bded1a5db1c08f13283fc7cee53da93dfe00785eb406512467ff8e445f8ad843744ac4179f30f942645dfd5bdf5f2bfc344ad02393053880a02d0012f035dc3fd54173c83d40217914653488fe9ce592dca34234163181d255281f2be7033725cfc4a6786509e7fabbaf0be8cf50882fc7b66fe94f259fd004e'  # noqa
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
        'nonce': 1,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 500000000,
        'amount': 0,
        'asset': {
            'ipfs': 'QmR45FmbVVrixReBwJkhEKde2qwHYaQzGxu4ZoDeswuF9w'
        },
        'signature': '0b6e81b123de99e953d3073a8760d3213ab5f5cf512e65a2dd73aebb410966d8fbc59e775deb4f23c51be0847402b5e1d4ee68732b3e6d8e8914d259d7e373eb',
        'id': '818228ce634b46c488f3b2df8fd02bd50331ebdedb44df5b9b11b97b01e9fb36',
        'serialized': 'ff02170100000005000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1920065cd1d000000000012202853f0f11ab91d73b73a2a86606103f45dd469ad2e89ec6f9a25febe8758d3fe0b6e81b123de99e953d3073a8760d3213ab5f5cf512e65a2dd73aebb410966d8fbc59e775deb4f23c51be0847402b5e1d4ee68732b3e6d8e8914d259d7e373eb'
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
        'nonce': 1,
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
        'signature': '672e89e66a9c5d7d95c21ccd07a89a111f02823146c06f14689d2cf1efd645fb648258fcf2280486d2cae19f391796d72145d2a8e6f261e887e34cd1998bdb65',
        'id': 'e8c7293d428048f8678dc6c88cb8b32bd49c8ae9b02018297c1889d9bd33ba8d',
        'serialized': 'ff02170100000006000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1928096980000000000000200010000000000000017134b5be4b327ddf9c2bb47fec8a1a44189e90f74020000000000000017bfa6aec83cf1bd03a0cab9f35c85ff51a3e9f041672e89e66a9c5d7d95c21ccd07a89a111f02823146c06f14689d2cf1efd645fb648258fcf2280486d2cae19f391796d72145d2a8e6f261e887e34cd1998bdb65'
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
        'nonce': 1,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 2500000000,
        'amount': 0,
        'signature': 'bdc048ca7eb5688cc01921aecf5914118cfc78eacc23825efa6d75094a683127cc02512dc59e1e0631fa8956f482eabc54933d23011a8337ea9cab99abed504d',
        'id': '707b4deb339e717dfef44c40db0692015ce9bbab015c007b016b8a46b341e859',
        'serialized': 'ff02170100000007000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200f902950000000000bdc048ca7eb5688cc01921aecf5914118cfc78eacc23825efa6d75094a683127cc02512dc59e1e0631fa8956f482eabc54933d23011a8337ea9cab99abed504d'
    }
    return data


@pytest.fixture
def transaction_type_8():
    """Transaction of type "HTLC lock"
    """
    data = {
        'version': 2,
        'network': 23,
        'typeGroup': 1,
        'type': 8,
        'nonce': 1,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 10000000,
        'amount': 200000000,
        'recipientId': 'AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC',
        'asset': {
            'lock': {
                'secretHash': '0f128d401958b1b30ad0d10406f47f9489321017b4614e6cb993fc63913c5454',
                'expiration': {
                    'type': 1,
                    'value': 1573455822
                }
            },
        },
        'signature': '7fe939b22a1da166b6ea58e3964651236fb4e0739f9716dedf92986f37df71ea7993e9a97b4a1686c0ad08028dcae08b7cb4a54b8a4db57e72b839a611e86358',
        'id': 'e1b34afa54bbf34de5c00716b92246c5248c2135221ece169db877ca60a14007',
        'serialized': 'ff02170100000008000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19280969800000000000000c2eb0b000000000f128d401958b1b30ad0d10406f47f9489321017b4614e6cb993fc63913c545401ce07c95d170995750207ecaf0ccf251c1265b92ad84f5536627fe939b22a1da166b6ea58e3964651236fb4e0739f9716dedf92986f37df71ea7993e9a97b4a1686c0ad08028dcae08b7cb4a54b8a4db57e72b839a611e86358'

    }
    return data

@pytest.fixture
def transaction_type_9():
    """Transaction of type "HTLC claim"
    """
    data = {
        'version': 2,
        'network': 23,
        'typeGroup': 1,
        'type': 9,
        'nonce': 1,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 0,
        'amount': 0,
        'asset': {
            'claim': {
                'lockTransactionId': '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4',
                'unlockSecret': 'my secret that should be 32bytes'
            },
        },
        'signature': '381188e6a3c0da8823ab37cf7562724b3920f4fc8a40cb259ae297bd7237b511cbfdbcb46b7afa319ad1c2d8cc3d8cdc33a437c8b17867777b891d03c036dfb9',
        'id': '846c5ee8a328376416735da43056d154d41e264564def42fb28b373c0d895c46',
        'serialized': 'ff02170100000009000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192000000000000000000943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb46d792073656372657420746861742073686f756c642062652033326279746573381188e6a3c0da8823ab37cf7562724b3920f4fc8a40cb259ae297bd7237b511cbfdbcb46b7afa319ad1c2d8cc3d8cdc33a437c8b17867777b891d03c036dfb9'

    }
    return data

@pytest.fixture
def transaction_type_10():
    """Transaction of type "HTLC refund"
    """
    data = {
        'version': 2,
        'network': 23,
        'typeGroup': 1,
        'type': 10,
        'nonce': 1,
        'senderPublicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'fee': 0,
        'amount': 0,
        'asset': {
            'refund': {
                'lockTransactionId': '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4',
            },
        },
        'signature': '16d9ef1dceb0cbb105a45af6bdde9439055f07197643f9e2837312463330fd02ec7b13d1242becfe333c1b8ab2ea91c0c8240390d86f0fb0f6cdc22ec6ac64f1',
        'id': '9356aa730990a2ea8e9871ffa65800f34ef1a4bec3215d89c950e72d82a34e91',
        'serialized': 'ff0217010000000a000100000000000000034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192000000000000000000943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb416d9ef1dceb0cbb105a45af6bdde9439055f07197643f9e2837312463330fd02ec7b13d1242becfe333c1b8ab2ea91c0c8240390d86f0fb0f6cdc22ec6ac64f1'

    }
    return data


@pytest.fixture
def message():
    data = {
        'camelCase_pk': {
            'publicKey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
            'signature': '304402200fb4adddd1f1d652b544ea6ab62828a0a65b712ed447e2538db0caebfa68929e02205ecb2e1c63b29879c2ecf1255db506d671c8b3fa6017f67cfd1bf07e6edd1cc8',  # noqa
            'message': 'Hello World'
        },

        'snake_case_pk': {
          'publickey': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
          'signature': '304402200fb4adddd1f1d652b544ea6ab62828a0a65b712ed447e2538db0caebfa68929e02205ecb2e1c63b29879c2ecf1255db506d671c8b3fa6017f67cfd1bf07e6edd1cc8',  # noqa
          'message': 'Hello World'
        },
        'passphrase': 'this is a top secret passphrase'
    }
    return data
