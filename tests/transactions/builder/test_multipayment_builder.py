from crypto.transactions.builder.multipayment_builder import MultipaymentBuilder

def test_it_should_sign_it_with_a_passphrase(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/multipayment')

    builder = (
        MultipaymentBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .gas_limit(fixture['data']['gasLimit'])
            .nonce(fixture['data']['nonce'])
            .pay('0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22', '100000')
            .pay('0xc3bbe9b1cee1ff85ad72b87414b0e9b7f2366763', '200000')
            .sign(passphrase)
    )

    assert builder.transaction.data['gasPrice'] == int(fixture['data']['gasPrice'])
    assert builder.transaction.data['gasLimit'] == int(fixture['data']['gasLimit'])
    assert builder.transaction.data['nonce'] == fixture['data']['nonce']
    assert builder.transaction.data['v'] == fixture['data']['v']
    assert builder.transaction.data['r'] == fixture['data']['r']
    assert builder.transaction.data['s'] == fixture['data']['s']

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['hash'] == fixture['data']['hash']
    assert builder.verify()

def test_it_should_handle_single_recipient(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/multipayment-single')

    builder = (
        MultipaymentBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .gas_limit(fixture['data']['gasLimit'])
            .nonce(fixture['data']['nonce'])
            .pay('0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22', '100000')
            .sign(passphrase)
    )

    assert builder.transaction.data['gasPrice'] == int(fixture['data']['gasPrice'])
    assert builder.transaction.data['gasLimit'] == int(fixture['data']['gasLimit'])
    assert builder.transaction.data['nonce'] == fixture['data']['nonce']
    assert builder.transaction.data['v'] == fixture['data']['v']
    assert builder.transaction.data['r'] == fixture['data']['r']
    assert builder.transaction.data['s'] == fixture['data']['s']

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['hash'] == fixture['data']['hash']
    assert builder.verify()

def test_it_should_handle_empty_payment(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/multipayment-empty')

    builder = (
        MultipaymentBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .gas_limit(fixture['data']['gasLimit'])
            .nonce(fixture['data']['nonce'])
            .sign(passphrase)
    )

    assert builder.transaction.data['gasPrice'] == int(fixture['data']['gasPrice'])
    assert builder.transaction.data['gasLimit'] == int(fixture['data']['gasLimit'])
    assert builder.transaction.data['nonce'] == fixture['data']['nonce']
    assert builder.transaction.data['v'] == fixture['data']['v']
    assert builder.transaction.data['r'] == fixture['data']['r']
    assert builder.transaction.data['s'] == fixture['data']['s']

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['hash'] == fixture['data']['hash']
    assert builder.verify()
