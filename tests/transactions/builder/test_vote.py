from crypto.conf import use_network
from crypto.constants import TRANSACTION_VOTE
from crypto.transactions.builder.vote import VoteTransaction


def test_vote_transaction():
    """Test if a vote transaction gets built
    """
    use_network('devnet')
    vote = '+034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192'
    transaction = VoteTransaction(vote)
    transaction.sign('testing')
    transaction_dict = transaction.to_dict()
    assert transaction_dict['signature']
    assert transaction_dict['asset']['votes']
    assert transaction_dict['type'] is TRANSACTION_VOTE
    transaction.verify()  # if no exception is raised, it means the transaction is valid
