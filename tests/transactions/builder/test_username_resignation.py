from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_USERNAME_RESIGNATION, TRANSACTION_TYPE_GROUP
from crypto.networks.devnet import Devnet
from crypto.transactions.builder.username_resignation import UsernameResignation

set_network(Devnet)


def test_username_resignation_transaction():
    """Test if username resignation transaction gets built
    """
    transaction = UsernameResignation()
    transaction.set_nonce(1)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_USERNAME_RESIGNATION
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 2500000000

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid


def test_username_resignation_transaction_custom_fee():
    """Test if username resignation transaction gets built with a custom fee
    """
    transaction = UsernameResignation(5)
    transaction.set_nonce(1)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_USERNAME_RESIGNATION
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 5

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid
