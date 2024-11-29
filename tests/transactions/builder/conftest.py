import pytest
import json
import os
from crypto.configuration.network import set_network
from crypto.networks.devnet import Devnet

@pytest.fixture(scope='session', autouse=True)
def configure_network():
    """
    Configures the network to Devnet before running any tests.
    This fixture runs automatically once per test session.
    """
    set_network(Devnet)

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
            '../../fixtures',
            f'{fixture_name}.json'
        )
        with open(fixtures_path, 'r') as f:
            return json.load(f)
    return _load_transaction_fixture

@pytest.fixture
def passphrase():
    """Passphrase used for tests"""

    return 'my super secret passphrase'
