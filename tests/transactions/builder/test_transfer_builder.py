from crypto.transactions.builder.transfer_builder import TransferBuilder

def test_it_should_sign_it_with_a_passphrase(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transfer')

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

    assert builder.transaction.data['gasPrice'] == fixture['data']['gasPrice']
    assert builder.transaction.data['nonce'] == fixture['data']['nonce']
    assert builder.transaction.data['network'] == fixture['data']['network']
    assert builder.transaction.data['gasLimit'] == fixture['data']['gasLimit']
    assert builder.transaction.data['recipientAddress'] == fixture['data']['recipientAddress']
    assert builder.transaction.data['value'] == fixture['data']['value']
    assert builder.transaction.data['v'] == fixture['data']['v']
    assert builder.transaction.data['r'] == fixture['data']['r']
    assert builder.transaction.data['s'] == fixture['data']['s']

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['id'] == fixture['data']['id']
    assert builder.verify()
