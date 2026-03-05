from crypto.transactions.builder.token_transfer_builder import (
    TokenTransferBuilder,
)


def test_token_transfer_transaction(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/token-transfer')

    builder = (
        TokenTransferBuilder
            .new()
            .recipient(fixture['data']['to'], int(fixture['data']['value']))
            .to(fixture['data']['to'])
            .nonce(fixture['data']['nonce'])
            .gas_price(fixture['data']['gasPrice'])
            .gas_limit(fixture['data']['gasLimit'])
            .sign(passphrase)
    )

    assert builder.transaction.data['gasPrice'] == int(
        fixture['data']['gasPrice']
    )
    assert builder.transaction.data['gasLimit'] == int(
        fixture['data']['gasLimit']
    )
    assert builder.transaction.data['nonce'] == fixture['data']['nonce']
    assert builder.transaction.data['to'].lower() == (
        fixture['data']['to'].lower()
    )
    assert builder.transaction.data['v'] == fixture['data']['v']
    assert builder.transaction.data['r'] == fixture['data']['r']
    assert builder.transaction.data['s'] == fixture['data']['s']
    assert builder.transaction.data['hash'] == fixture['data']['hash']

    assert builder.verify()


def test_token_transfer_serialization(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/token-transfer')

    builder = (
        TokenTransferBuilder
            .new()
            .recipient(fixture['data']['to'], int(fixture['data']['value']))
            .to(fixture['data']['to'])
            .nonce(fixture['data']['nonce'])
            .gas_price(fixture['data']['gasPrice'])
            .gas_limit(fixture['data']['gasLimit'])
            .sign(passphrase)
    )

    serialized = builder.transaction.serialize().hex()
    assert serialized == fixture['serialized']
