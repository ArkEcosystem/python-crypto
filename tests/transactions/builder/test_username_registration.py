from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_USERNAME_REGISTRATION, TRANSACTION_TYPE_GROUP
from crypto.networks.devnet import Devnet
from crypto.transactions.builder.username_registration import UsernameRegistration

set_network(Devnet)


def test_username_registration_transaction(passphrase):
    """Test if a username registration transaction gets built
    """
    username_name = 'mr.username'

    transaction = UsernameRegistration(username_name)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.sign(passphrase)
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['asset']['username'] == username_name
    assert transaction_dict['type'] is TRANSACTION_USERNAME_REGISTRATION
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 2500000000

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid


def test_username_registration_transaction_custom_fee(passphrase):
    """Test if a username registration transaction gets built with a custom fee
    """
    username_name = 'mr.username'

    transaction = UsernameRegistration(username_name, 5)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.sign(passphrase)
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['asset']['username'] == username_name
    assert transaction_dict['type'] is TRANSACTION_USERNAME_REGISTRATION
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 5

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid
