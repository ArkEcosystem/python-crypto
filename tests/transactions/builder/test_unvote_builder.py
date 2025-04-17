from crypto.transactions.builder.unvote_builder import UnvoteBuilder

def test_unvote_transaction(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/unvote')

    builder = (
        UnvoteBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .nonce(fixture['data']['nonce'])
            .network(fixture['data']['network'])
            .gas(fixture['data']['gas'])
            .recipient_address(fixture['data']['recipientAddress'])
            .sign(passphrase)
    )

    assert builder.transaction.data['gasPrice'] == fixture['data']['gasPrice']
    assert builder.transaction.data['nonce'] == fixture['data']['nonce']
    assert builder.transaction.data['network'] == fixture['data']['network']
    assert builder.transaction.data['gas'] == fixture['data']['gas']
    assert builder.transaction.data['recipientAddress'] == fixture['data']['recipientAddress']
    assert builder.transaction.data['value'] == int(fixture['data']['value'])
    assert builder.transaction.data['v'] == fixture['data']['v']
    assert builder.transaction.data['r'] == fixture['data']['r']
    assert builder.transaction.data['s'] == fixture['data']['s']

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['id'] == fixture['data']['id']
    assert builder.verify()

def test_unvote_transaction_with_default_recipient_address(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/unvote')

    builder = (
        UnvoteBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .nonce(fixture['data']['nonce'])
            .network(fixture['data']['network'])
            .gas(fixture['data']['gas'])
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

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['id'] == fixture['data']['id']
    assert builder.verify()
