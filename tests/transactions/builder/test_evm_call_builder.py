from crypto.transactions.builder.evm_call_builder import EvmCallBuilder

def test_evm_call_transaction(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/evm-sign')

    builder = (
        EvmCallBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .nonce(fixture['data']['nonce'])
            .network(fixture['data']['network'])
            .payload(fixture['data']['data'])
            .gas(fixture['data']['gas'])
            .recipient_address('0xE536720791A7DaDBeBdBCD8c8546fb0791a11901')
            .sign(passphrase)
    )

    assert builder.transaction.data['gasPrice'] == fixture['data']['gasPrice']
    assert builder.transaction.data['nonce'] == fixture['data']['nonce']
    assert builder.transaction.data['network'] == fixture['data']['network']
    assert builder.transaction.data['gas'] == fixture['data']['gas']
    assert builder.transaction.data['recipientAddress'].lower() == fixture['data']['recipientAddress'].lower()
    assert builder.transaction.data['value'] == int(fixture['data']['value'])
    assert builder.transaction.data['v'] == fixture['data']['v']
    assert builder.transaction.data['r'] == fixture['data']['r']
    assert builder.transaction.data['s'] == fixture['data']['s']

    assert builder.verify()
