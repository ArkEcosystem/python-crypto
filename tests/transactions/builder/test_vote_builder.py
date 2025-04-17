from crypto.transactions.builder.vote_builder import VoteBuilder

def test_vote_transaction(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/vote')

    builder = (
        VoteBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .nonce(fixture['data']['nonce'])
            .network(fixture['data']['network'])
            .gas(fixture['data']['gas'])
            .to(fixture['data']['to'])
            .vote('0xC3bBE9B1CeE1ff85Ad72b87414B0E9B7F2366763')  # Example vote address
            .sign(passphrase)
    )

    assert builder.transaction.data['gasPrice'] == fixture['data']['gasPrice']
    assert builder.transaction.data['nonce'] == fixture['data']['nonce']
    assert builder.transaction.data['network'] == fixture['data']['network']
    assert builder.transaction.data['gas'] == fixture['data']['gas']
    assert builder.transaction.data['to'] == fixture['data']['to']
    assert builder.transaction.data['value'] == int(fixture['data']['value'])
    assert builder.transaction.data['v'] == fixture['data']['v']
    assert builder.transaction.data['r'] == fixture['data']['r']
    assert builder.transaction.data['s'] == fixture['data']['s']

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['id'] == fixture['data']['id']
    assert builder.verify()

def test_vote_transaction_with_default_to(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/vote')

    builder = (
        VoteBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .nonce(fixture['data']['nonce'])
            .network(fixture['data']['network'])
            .gas(fixture['data']['gas'])
            .vote('0xC3bBE9B1CeE1ff85Ad72b87414B0E9B7F2366763')  # Example vote address
            .sign(passphrase)
    )

    assert builder.transaction.data['gasPrice'] == fixture['data']['gasPrice']
    assert builder.transaction.data['nonce'] == fixture['data']['nonce']
    assert builder.transaction.data['network'] == fixture['data']['network']
    assert builder.transaction.data['gas'] == fixture['data']['gas']
    assert builder.transaction.data['to'].lower() == fixture['data']['to'].lower()
    assert builder.transaction.data['value'] == int(fixture['data']['value'])
    assert builder.transaction.data['v'] == fixture['data']['v']
    assert builder.transaction.data['r'] == fixture['data']['r']
    assert builder.transaction.data['s'] == fixture['data']['s']

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['id'] == fixture['data']['id']
    assert builder.verify()
