from crypto.transactions.builder.evm_call_builder import EvmCallBuilder

def test_evm_call_transaction(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/evm-sign')

    builder = (
        EvmCallBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .gas_limit(fixture['data']['gasLimit'])
            .nonce(fixture['data']['nonce'])
            .payload(fixture['data']['data'])
            .to('0xE536720791A7DaDBeBdBCD8c8546fb0791a11901')
            .sign(passphrase)
    )

    assert builder.transaction.data['gasPrice'] == int(fixture['data']['gasPrice'])
    assert builder.transaction.data['gasLimit'] == int(fixture['data']['gasLimit'])
    assert builder.transaction.data['nonce'] == fixture['data']['nonce']
    assert builder.transaction.data['to'].lower() == fixture['data']['to'].lower()
    assert builder.transaction.data['value'] == int(fixture['data']['value'])
    assert builder.transaction.data['v'] == fixture['data']['v']
    assert builder.transaction.data['r'] == fixture['data']['r']
    assert builder.transaction.data['s'] == fixture['data']['s']

    assert builder.verify()
