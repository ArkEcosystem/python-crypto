from crypto.transactions.builder.vote_builder import VoteBuilder

def test_vote_transaction(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('vote')

    builder = (
        VoteBuilder()
        .gas_price(fixture['data']['gasPrice'])
        .nonce(fixture['data']['nonce'])
        .network(fixture['data']['network'])
        .gas_limit(fixture['data']['gasLimit'])
        .recipient_address(fixture['data']['recipientAddress'])
        .vote('0x512F366D524157BcF734546eB29a6d687B762255')  # Example vote address
        .sign(passphrase)
    )

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['id'] == fixture['data']['id']
    assert builder.verify()