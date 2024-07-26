from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_TYPE_GROUP, TRANSACTION_VOTE
from crypto.networks.devnet import Devnet
from crypto.transactions.builder.vote import Vote

set_network(Devnet)


def test_vote_transaction(passphrase):
    """Test if a vote transaction gets built
    """
    votes = ['034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192']

    transaction = Vote(votes, None)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.sign(passphrase)
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['asset']['votes'] == votes
    assert transaction_dict['asset']['unvotes'] == []
    assert transaction_dict['type'] is TRANSACTION_VOTE
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 100000000
    assert transaction_dict['expiration'] == 0
    assert transaction_dict['senderPublicKey'] == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid

def test_unvote_transaction(passphrase):
    """Test if a vote transaction gets built
    """
    unvotes = ['02dfc9a0684fe0744101b2398e9c86a81b5e46aceffff994ef9189083f01d0bebb']

    transaction = Vote(None, unvotes)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.sign(passphrase)
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['asset']['votes'] == []
    assert transaction_dict['asset']['unvotes'] == unvotes
    assert transaction_dict['type'] is TRANSACTION_VOTE
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 100000000
    assert transaction_dict['expiration'] == 0
    assert transaction_dict['senderPublicKey'] == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid

def test_vote_swap_transaction(passphrase):
    """Test if a vote transaction gets built
    """
    votes = ['034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192']
    unvotes = ['02dfc9a0684fe0744101b2398e9c86a81b5e46aceffff994ef9189083f01d0bebb']

    transaction = Vote(votes, unvotes)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.sign(passphrase)
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['asset']['votes'] == votes
    assert transaction_dict['asset']['unvotes'] == unvotes
    assert transaction_dict['type'] is TRANSACTION_VOTE
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 100000000
    assert transaction_dict['expiration'] == 0
    assert transaction_dict['senderPublicKey'] == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid

def test_vote_transaction_custom_fee(passphrase):
    """Test if a vote transaction gets built with a custom fee
    """
    votes = ['034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192']

    transaction = Vote(votes, None, 5)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.sign(passphrase)
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['asset']['votes'] == votes
    assert transaction_dict['asset']['unvotes'] == []
    assert transaction_dict['type'] is TRANSACTION_VOTE
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 5
    assert transaction_dict['expiration'] == 0
    assert transaction_dict['senderPublicKey'] == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid
