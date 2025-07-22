from crypto.transactions.builder.validator_registration_builder import ValidatorRegistrationBuilder

def test_validator_registration_transaction(passphrase, validator_public_key, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/validator-registration')

    builder = (
        ValidatorRegistrationBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .gas_limit(fixture['data']['gasLimit'])
            .nonce(fixture['data']['nonce'])
            .value(fixture['data']['value'])
            .validator_public_key(validator_public_key)
            .to(fixture['data']['to'])
            .sign(passphrase)
    )

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['gasPrice'] == int(fixture['data']['gasPrice'])
    assert builder.transaction.data['gasLimit'] == int(fixture['data']['gasLimit'])
    assert builder.transaction.data['nonce'] == fixture['data']['nonce']
    assert builder.transaction.data['to'] == fixture['data']['to']
    assert builder.transaction.data['value'] == int(fixture['data']['value'])
    assert builder.transaction.data['v'] == fixture['data']['v']
    assert builder.transaction.data['r'] == fixture['data']['r']
    assert builder.transaction.data['s'] == fixture['data']['s']

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['hash'] == fixture['data']['hash']
    assert builder.verify()

def test_validator_registration_transaction_with_default_to(passphrase, validator_public_key, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/validator-registration')

    builder = (
        ValidatorRegistrationBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .gas_limit(fixture['data']['gasLimit'])
            .nonce(fixture['data']['nonce'])
            .value(fixture['data']['value'])
            .validator_public_key(validator_public_key)
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

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['hash'] == fixture['data']['hash']
    assert builder.verify()
