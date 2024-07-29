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
