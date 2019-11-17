from crypto.constants import TRANSACTION_VOTE, TRANSACTION_TYPE_GROUP
from crypto.transactions.builder.vote import Vote


def test_vote_transaction():
    """Test if a vote transaction gets built
    """
    vote = '+034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192'
    transaction = Vote(vote)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(123)
    transaction.sign('testing')
    transaction_dict = transaction.to_dict()
    assert transaction_dict['nonce'] == 123
    assert transaction_dict['signature']
    assert transaction_dict['asset']['votes']
    assert transaction_dict['type'] is TRANSACTION_VOTE
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    transaction.verify()  # if no exception is raised, it means the transaction is valid
