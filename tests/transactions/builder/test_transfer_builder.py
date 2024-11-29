import pytest
import json
import os

from crypto.transactions.builder.transfer_builder import TransferBuilder
from crypto.configuration.network import set_network
from crypto.networks.devnet import Devnet

set_network(Devnet)


def get_transaction_fixture(fixture_name):
    fixtures_path = os.path.join(
        os.path.dirname(__file__),
        '../../fixtures',
        f'{fixture_name}.json'
    )
    with open(fixtures_path, 'r') as f:
        return json.load(f)


def test_transfer_transaction(passphrase):
    # Cargar el fixture
    fixture = get_transaction_fixture('transfer')

    builder = (
        TransferBuilder()
        .gas_price(fixture['data']['gasPrice'])
        .nonce(fixture['data']['nonce'])
        .network(fixture['data']['network'])
        .gas_limit(fixture['data']['gasLimit'])
        .recipient_address(fixture['data']['recipientAddress'])
        .value(fixture['data']['value'])
        .sign(passphrase)
    )

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['id'] == fixture['data']['id']
    assert builder.verify()
