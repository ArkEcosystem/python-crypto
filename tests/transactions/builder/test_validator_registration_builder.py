from crypto.transactions.builder.validator_registration_builder import ValidatorRegistrationBuilder

def test_validator_registration_transaction(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('validator-registration')

    builder = (
        ValidatorRegistrationBuilder()
        .gas_price(fixture['data']['gasPrice'])
        .nonce(fixture['data']['nonce'])
        .network(fixture['data']['network'])
        .gas_limit(fixture['data']['gasLimit'])
        .validator_public_key('a08058db53e2665c84a40f5152e76dd2b652125a6079130d4c315e728bcf4dd1dfb44ac26e82302331d61977d3141118')
        .recipient_address(fixture['data']['recipientAddress'])
        .sign(passphrase)
    )

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['id'] == fixture['data']['id']
    assert builder.verify()