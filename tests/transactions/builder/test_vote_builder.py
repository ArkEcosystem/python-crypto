from crypto.transactions.builder.vote_builder import VoteBuilder

def test_vote_transaction(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/vote')

    builder = (
        VoteBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .gas_limit(fixture['data']['gasLimit'])
            .nonce(fixture['data']['nonce'])
            .to(fixture['data']['to'])
            .vote('0xC3bBE9B1CeE1ff85Ad72b87414B0E9B7F2366763')  # Example vote address
            .sign(passphrase)
    )

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

def test_vote_transaction_with_default_to(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/vote')

    builder = (
        VoteBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .gas_limit(fixture['data']['gasLimit'])
            .nonce(fixture['data']['nonce'])
            .vote('0xC3bBE9B1CeE1ff85Ad72b87414B0E9B7F2366763')  # Example vote address
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
