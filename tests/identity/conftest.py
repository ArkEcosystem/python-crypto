import pytest

@pytest.fixture
def identity():
    """Identity fixture
    """
    data = {
        'data': {
            'private_key': 'bef98d4c0e58d0e4695560594f91a349421b7cdc3e63a560470ccb259f99f087',
            'public_key': '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3',
            'address': 'DBhj9G4xJNHgbBLgsofZUSSQtAfzZz5yEG',
            'wif': 'UdFWh1JiogHqCye7kv8RoUq9zr2z6gVsMQsZARuF7xF9JTk97NWT'
        },
        'passphrase': 'my super secret passphrase'
    }
    return data
