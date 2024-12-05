from crypto.transactions.builder.transfer_builder import TransferBuilder

def test_transfer_transaction(passphrase, load_transaction_fixture):
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

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['id'] == fixture['data']['id']
    assert builder.verify()
