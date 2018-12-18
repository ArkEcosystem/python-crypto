import pytest


@pytest.fixture
def transaction_type_0():
    """Transaction of type "transfer"
    """
    data = {
        'version': 1,
        'network': 30,
        'type': 0,
        'timestamp': 0,
        'senderPublicKey': '03cb7bca143376721d0e9e3f3ccb0dc2e7e8470c06e630c3cef73f03e309b558ad',
        'fee': 0,
        'amount': 12500000000000000,
        'expiration': 0,
        'recipientId': 'DGihocTkwDygiFvmg6aG8jThYTic47GzU9',
        'signature': '3044022016ecdf3039e69514c7d75861b22fc076496b61c07a1fcf793dc4f5c76fa0532b0220579c4c0c9d13720f9db5d9df29ed8ceab0adc266c6c160d612d4894dc5867eb1',  # noqa
        'id': 'e40ce11cab82736da1cc91191716f3c1f446ca7b6a9f4f93b7120ef105ba06e8',
        'serialized': 'ff011e000000000003cb7bca143376721d0e9e3f3ccb0dc2e7e8470c06e630c3cef73f03e309b558ad0000000000000000000040b10baf682c00000000001e7f048c40fd8a0442ffe79e0aa804f27fd5db15943044022016ecdf3039e69514c7d75861b22fc076496b61c07a1fcf793dc4f5c76fa0532b0220579c4c0c9d13720f9db5d9df29ed8ceab0adc266c6c160d612d4894dc5867eb1'  # noqa
    }
    return data


@pytest.fixture
def transaction_type_1():
    """Transaction of type "second signature registration"
    """
    data = {
        'version': 1,
        'network': 30,
        'type': 1,
        'timestamp': 4895203,
        'senderPublicKey': '03a02b9d5fdd1307c2ee4652ba54d492d1fd11a7d1bb3f3a44c4a05e79f19de933',
        'fee': 500000000,
        'asset': {
            'signature': {
                'publicKey': '0292d580f200d041861d78b3de5ff31c6665b7a092ac3890d9132593beb9aa8513'
            }
        },
        'signature': '3045022100e4fe1f3fb2845ad5f6ab377f247ffb797661d7516626bdc1d2f0f73eca582b4d02200ada103bdbff439d57c7aaa266f30ce74ff4385f0c77a486070033061b71650c',  # noqa
        'amount': 0,
        'recipientId': 'D7seWn8JLVwX4nHd9hh2Lf7gvZNiRJ7qLk',
        'id': '62c36be3e5176771a476d813f64082a8f4e3861c0356438bdf1cc91eebcc9b0d',
        'serialized': 'ff011e01e3b14a0003a02b9d5fdd1307c2ee4652ba54d492d1fd11a7d1bb3f3a44c4a05e79f19de9330065cd1d00000000000292d580f200d041861d78b3de5ff31c6665b7a092ac3890d9132593beb9aa85133045022100e4fe1f3fb2845ad5f6ab377f247ffb797661d7516626bdc1d2f0f73eca582b4d02200ada103bdbff439d57c7aaa266f30ce74ff4385f0c77a486070033061b71650c'  # noqa
    }
    return data


@pytest.fixture
def transaction_type_2():
    """Transaction of type "delegate registration"
    """
    data = {
        'version': 1,
        'network': 30,
        'type': 2,
        'timestamp': 0,
        'senderPublicKey': '03e5b39a83e6c7c952c5908089d4524bb8dda93acc2b2b953247e43dc4fe9aa3d1',
        'fee': 0,
        'asset': {
            'delegate': {
                'username': 'genesis_1'
            }
        },
        'signature': '3045022100e3e38811778023e6f17fefd447f179d45ab92c398c7cfb1e34e2f6e1b167c95a022070c36439ecec0fc3c43850070f29515910435d389e059579878d61b5ff2ea337',  # noqa
        'amount': 0,
        'id': 'eb0146ac79afc228f0474a5ae1c4771970ae7880450b998c401029f522cd8a21',
        'serialized': 'ff011e020000000003e5b39a83e6c7c952c5908089d4524bb8dda93acc2b2b953247e43dc4fe9aa3d10000000000000000000967656e657369735f313045022100e3e38811778023e6f17fefd447f179d45ab92c398c7cfb1e34e2f6e1b167c95a022070c36439ecec0fc3c43850070f29515910435d389e059579878d61b5ff2ea337'  # noqa
    }
    return data


@pytest.fixture
def transaction_type_3():
    """Transaction of type "vote"
    """
    data = {
        'version': 1,
        'network': 30,
        'type': 3,
        'timestamp': 4349399,
        'senderPublicKey': '0374e9a97611540a9ce4812b0980e62d3c5141ea964c2cab051f14a78284570dcd',
        'fee': 100000000,
        'asset': {
            'votes': ['+02dcb94d73fb54e775f734762d26975d57f18980314f3b67bc52beb393893bc706']
        },
        'signature': '3045022100af1e5d6f3c9eff8699192ad1b827e7cf7c60040bd2f704360a1f1fbadf6bc1cf022048238b7175369861436d895adaeeeb31ceb453e543dbf20218a4a5b688650482',  # noqa
        'amount': 0,
        'recipientId': 'DRac35wghMcmUSe5jDMLBDLWkVVjyKZFxK',
        'id': 'a430dbe34172d205ec251875b14438e58e4bd6cf4efc1ebb3da4c206b002115b',
        'serialized': 'ff011e03d75d42000374e9a97611540a9ce4812b0980e62d3c5141ea964c2cab051f14a78284570dcd00e1f5050000000000010102dcb94d73fb54e775f734762d26975d57f18980314f3b67bc52beb393893bc7063045022100af1e5d6f3c9eff8699192ad1b827e7cf7c60040bd2f704360a1f1fbadf6bc1cf022048238b7175369861436d895adaeeeb31ceb453e543dbf20218a4a5b688650482'  # noqa
    }
    return data


@pytest.fixture
def transaction_type_4():
    """Transaction of type "multi signature registration"
    """
    data = {
        'version': 1,
        'network': 23,
        'id': 'cbd6862966bb1b03ba742397b7e5a88d6eefb393a362ead0d605723b840db2af',
        'blockid': '1844069042066945391',
        'type': 4,
        'timestamp': 10112114,
        'amount': 0,
        'fee': 2000000000,
        'senderId': 'AMw3TiLrmVmwmFVwRzn96kkUsUpFTqsAEX',
        'senderPublicKey': '036928c98ee53a1f52ed01dd87db10ffe1980eb47cd7c0a7d688321f47b5d7d760',
        'signature': '30440220324d89c5792e4a54ae70b4f1e27e2f87a8b7169cc6f2f7b2c83dba894960f987022053b8d0ae23ff9d1769364db7b6fd03216d93753c82a711c3558045e787bc01a5',  # noqa
        'signSignature': '304402201fcd54a9ac9c0269b8cec213566ddf43207798e2cf9ca1ce3c5d315d66321c6902201aa94c4ed3e5e479a12220aa886b259e488eb89b697c711f91e8c03b9620e0b1',  # noqa
        'signatures': [
            '304502210097f17c8eecf36f86a967cc52a83fa661e4ffc70cc4ea08df58673669406d424c0220798f5710897b75dda42f6548f841afbe4ed1fa262097112cf5a1b3f7dade60e4',  # noqa
            '304402201a4a4c718bfdc699bbb891b2e89be018027d2dcd10640b5ddf07802424dab78e02204ec7c7d505d2158c3b51fdd3843d16aecd2eaaa4c6c7a555ef123c5e59fd41fb',  # noqa
            '304402207e660489bced5ce80c33d45c86781b63898775ab4a231bb48780f97b40073a63022026f0cefd0d83022d822522ab4366a82e3b89085c328817919939f2efeabd913d'  # noqa
        ],
        'asset': {
            'multisignature': {
                'min': 2,
                'keysgroup': [
                    '+03543c6cc3545be6bac09c82721973a052c690658283472e88f24d14739f75acc8',
                    '+0276dc5b8706a85ca9fdc46e571ac84e52fbb48e13ec7a165a80731b44ae89f1fc',
                    '+02e8d5d17eb17bbc8d7bf1001d29a2d25d1249b7bb7a5b7ad8b7422063091f4b31'
                ],
                'lifetime': 24
            }
        },
        'serialized': 'ff011704724c9a00036928c98ee53a1f52ed01dd87db10ffe1980eb47cd7c0a7d688321f47b5d7d76000943577000000000002031803543c6cc3545be6bac09c82721973a052c690658283472e88f24d14739f75acc80276dc5b8706a85ca9fdc46e571ac84e52fbb48e13ec7a165a80731b44ae89f1fc02e8d5d17eb17bbc8d7bf1001d29a2d25d1249b7bb7a5b7ad8b7422063091f4b3130440220324d89c5792e4a54ae70b4f1e27e2f87a8b7169cc6f2f7b2c83dba894960f987022053b8d0ae23ff9d1769364db7b6fd03216d93753c82a711c3558045e787bc01a5304402201fcd54a9ac9c0269b8cec213566ddf43207798e2cf9ca1ce3c5d315d66321c6902201aa94c4ed3e5e479a12220aa886b259e488eb89b697c711f91e8c03b9620e0b1ff304502210097f17c8eecf36f86a967cc52a83fa661e4ffc70cc4ea08df58673669406d424c0220798f5710897b75dda42f6548f841afbe4ed1fa262097112cf5a1b3f7dade60e4304402201a4a4c718bfdc699bbb891b2e89be018027d2dcd10640b5ddf07802424dab78e02204ec7c7d505d2158c3b51fdd3843d16aecd2eaaa4c6c7a555ef123c5e59fd41fb304402207e660489bced5ce80c33d45c86781b63898775ab4a231bb48780f97b40073a63022026f0cefd0d83022d822522ab4366a82e3b89085c328817919939f2efeabd913d'  # noqa
    }
    return data


@pytest.fixture
def transaction_type_5():
    """Transaction of type "ipfs"
    """
    data = {
        'data': {},
        'serialised': ''
    }
    return data


@pytest.fixture
def transaction_type_6():
    """Transaction of type "timelock transfer"
    """
    data = {
        'data': {},
        'serialised': ''
    }
    return data


@pytest.fixture
def transaction_type_7():
    """Transaction of type "multi payment"
    """
    data = {
        'data': {},
        'serialised': ''
    }
    return data


@pytest.fixture
def transaction_type_8():
    """Transaction of type "delegate resignation"
    """
    data = {
        'data': {},
        'serialised': ''
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
