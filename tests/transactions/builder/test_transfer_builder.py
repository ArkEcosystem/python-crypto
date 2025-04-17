from crypto.transactions.builder.transfer_builder import TransferBuilder
from crypto.utils.unit_converter import UnitConverter

def test_it_should_sign_it_with_a_passphrase(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/transfer')

    builder = (
        TransferBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .nonce(fixture['data']['nonce'])
            .network(fixture['data']['network'])
            .gas(fixture['data']['gas'])
            .to(fixture['data']['to'])
            .value(fixture['data']['value'])
            .sign(passphrase)
    )

    assert builder.transaction.data['gasPrice'] == fixture['data']['gasPrice']
    assert builder.transaction.data['nonce'] == fixture['data']['nonce']
    assert builder.transaction.data['network'] == fixture['data']['network']
    assert builder.transaction.data['gas'] == fixture['data']['gas']
    assert builder.transaction.data['to'] == fixture['data']['to']
    assert builder.transaction.data['value'] == int(fixture['data']['value'])
    assert builder.transaction.data['v'] == fixture['data']['v']
    assert builder.transaction.data['r'] == fixture['data']['r']
    assert builder.transaction.data['s'] == fixture['data']['s']

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['id'] == fixture['data']['id']
    assert builder.verify()

def test_it_should_handle_unit_converter(passphrase, address):
    builder = (
        TransferBuilder
            .new()
            .gas_price(UnitConverter.parse_units(5, 'gwei'))
            .nonce('1')
            .gas(UnitConverter.parse_units(0.1, 'gwei'))
            .to(address)
            .value(UnitConverter.parse_units(10, 'ark'))
            .sign(passphrase)
    )

    assert builder.transaction.data['gasPrice'] == 5000000000
    assert builder.transaction.data['nonce'] == '1'
    assert builder.transaction.data['gas'] == 100000000
    assert builder.transaction.data['value'] == 10000000000000000000

    assert builder.verify()
