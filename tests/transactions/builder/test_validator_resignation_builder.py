from crypto.transactions.builder.validator_resignation_builder import ValidatorResignationBuilder

def test_validator_resignation_transaction(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('validator-resignation')

    builder = (
        ValidatorResignationBuilder()
        .gas_price(fixture['data']['gasPrice'])
        .nonce(fixture['data']['nonce'])
        .network(fixture['data']['network'])
        .gas_limit(fixture['data']['gasLimit'])
        .recipient_address(fixture['data']['recipientAddress'])
        .sign(passphrase)
    )

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['id'] == fixture['data']['id']
    assert builder.verify()