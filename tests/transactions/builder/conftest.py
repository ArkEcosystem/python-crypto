import pytest

@pytest.fixture
def passphrase():
    """Passphrase used for tests"""

    return 'found lobster oblige describe ready addict body brave live vacuum display salute lizard combine gift resemble race senior quality reunion proud tell adjust angle'

@pytest.fixture
def validator_public_key():
    """BLS Public used for validator tests"""

    return '30954f46d6097a1d314e900e66e11e0dad0a57cd03e04ec99f0dedd1c765dcb11e6d7fa02e22cf40f9ee23d9cc1c0624'

@pytest.fixture
def username():
    """Username used for tests"""

    return 'fixture'

@pytest.fixture
def address():
    """Address used for tests"""

    return '0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22'
