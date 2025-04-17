from crypto.transactions.builder.username_resignation_builder import UsernameResignationBuilder

def test_username_resignation_transaction(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/username-resignation')

    builder = (
        UsernameResignationBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .nonce(fixture['data']['nonce'])
            .network(fixture['data']['network'])
            .gas(fixture['data']['gas'])
            .sign(passphrase)
    )

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['id'] == fixture['data']['id']
    assert builder.verify()
