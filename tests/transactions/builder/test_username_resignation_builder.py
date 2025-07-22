from crypto.transactions.builder.username_resignation_builder import UsernameResignationBuilder

def test_username_resignation_transaction(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/username-resignation')

    builder = (
        UsernameResignationBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .gas_limit(fixture['data']['gasLimit'])
            .nonce(fixture['data']['nonce'])
            .sign(passphrase)
    )

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['hash'] == fixture['data']['hash']
    assert builder.verify()
