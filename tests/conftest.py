import pytest
import json
import os
from crypto.configuration.network import Network
from crypto.networks.testnet import Testnet


@pytest.fixture(scope='session', autouse=True)
def configure_network():
    """
    Configures the network to Testnet before running any tests.
    This fixture runs automatically once per test session.
    """
    Network.set_network(Testnet())

@pytest.fixture
def load_transaction_fixture():
    """
    Fixture to load a transaction fixture from the fixtures directory.

    Usage in tests:
        def test_example(load_transaction_fixture):
            fixture = load_transaction_fixture('fixture_name')
    """
    def _load_transaction_fixture(fixture_name):
        fixtures_path = os.path.join(
            os.path.dirname(__file__),
            './fixtures',
            f'{fixture_name}.json'
        )
        with open(fixtures_path, 'r') as f:
            return json.load(f)
    return _load_transaction_fixture

@pytest.fixture
def passphrase():
    """Passphrase used for tests"""

    return 'found lobster oblige describe ready addict body brave live vacuum display salute lizard combine gift resemble race senior quality reunion proud tell adjust angle'
