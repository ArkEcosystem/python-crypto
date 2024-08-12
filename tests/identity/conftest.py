import pytest

@pytest.fixture
def identity():
    """Identity fixture
    """
    data = {
        'data': {
            'private_key': 'bef98d4c0e58d0e4695560594f91a349421b7cdc3e63a560470ccb259f99f087',
            'public_key': '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3',
            'address': '0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22',
            'wif': 'SFyRYRYL1DddchRpuhp94hKN1tpYjzAEkLuUDAMjGJBkoAaz2RQk'
        },
        'passphrase': 'my super secret passphrase'
    }
    return data

@pytest.fixture
def validator():
    """Validator fixture
    """
    return {
        'bls_public_key': 'b0093ac8f37588e15df7cfb04d0722dc5486cec062233136d3b6a16d41946577a1f332c4c29c0601ccefac1905dbb611',
        'bls_private_key': '3c0e55f46009b02bd739a16945babe797e6cbd096294dcc2550bce4baea2bde9',
        'passphrase': 'bless organ december boring ill obvious unaware dinosaur broccoli build hamster rebuild skin airport stay entry denial agent october thought duck trouble decorate way',
    }
