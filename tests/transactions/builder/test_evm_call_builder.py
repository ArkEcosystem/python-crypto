from crypto.transactions.builder.evm_call_builder import EvmCallBuilder

def test_evm_call_transaction(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('evm-sign')

    builder = (
        EvmCallBuilder()
        .gas_price(fixture['data']['gasPrice'])
        .nonce(fixture['data']['nonce'])
        .network(fixture['data']['network'])
        .payload(fixture['data']['data'])
        .gas_limit(fixture['data']['gasLimit'])
        .recipient_address('0xE536720791A7DaDBeBdBCD8c8546fb0791a11901')
        .sign(passphrase)
    )

    assert builder.verify()