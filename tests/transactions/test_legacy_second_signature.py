import pytest

from crypto.configuration.network import Network
from crypto.identity.private_key import PrivateKey
from crypto.networks.testnet import Testnet
from crypto.transactions.deserializer import Deserializer
from crypto.transactions.types.transfer import Transfer


@pytest.fixture
def fixture(load_transaction_fixture):
    """Test vector from the Mainsail LSS v1 spec, built for chain 10_000"""

    return load_transaction_fixture('transactions/transfer-legacy-second-signature-vector')


@pytest.fixture(autouse=True)
def vector_network(fixture):
    class VectorNetwork(Testnet):
        def chain_id(self):
            return fixture['chainId']

    Network.set_network(VectorNetwork())

    yield

    Network.set_network(Testnet())


@pytest.fixture
def unsigned_data(fixture):
    return {
        key: value
        for key, value in fixture['data'].items()
        if key not in ('legacySecondSignature', 'hash')
    }


def test_it_should_sign_the_signed_transaction_hash_with_the_second_key(fixture, unsigned_data):
    transaction = Transfer(unsigned_data)

    transaction.sign(PrivateKey.from_hex(fixture['privateKey']))

    assert transaction.serialize().hex() == fixture['signed']
    assert transaction.get_id() == fixture['data']['hash']

    transaction.legacy_second_sign(PrivateKey.from_hex(fixture['secondPrivateKey']))

    assert transaction.data['legacySecondSignature'] == fixture['data']['legacySecondSignature']
    assert transaction.serialize().hex() == fixture['serialized']
    assert transaction.get_id() == fixture['data']['hash']


def test_it_should_use_a_0_or_1_recovery_id(fixture, unsigned_data):
    transaction = Transfer(unsigned_data)

    transaction.sign(PrivateKey.from_hex(fixture['privateKey']))
    transaction.legacy_second_sign(PrivateKey.from_hex(fixture['secondPrivateKey']))

    assert transaction.data['legacySecondSignature'][-2:] in ('00', '01')


def test_it_should_require_the_primary_signature_first(fixture, unsigned_data):
    transaction = Transfer(unsigned_data)

    error = 'Transaction must be signed before adding a legacy second signature'

    with pytest.raises(ValueError, match=error):
        transaction.legacy_second_sign(PrivateKey.from_hex(fixture['secondPrivateKey']))


def test_it_should_deserialize_and_hash_only_the_first_9_fields(fixture):
    transaction = Deserializer.new(fixture['serialized']).deserialize()

    assert transaction.data['legacySecondSignature'] == fixture['data']['legacySecondSignature']
    assert transaction.data['hash'] == fixture['data']['hash']
    assert transaction.serialize().hex() == fixture['serialized']
    assert transaction.verify()
