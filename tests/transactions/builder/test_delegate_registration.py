from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_DELEGATE_REGISTRATION, TRANSACTION_TYPE_GROUP
from crypto.networks.devnet import Devnet
from crypto.transactions.builder.delegate_registration import DelegateRegistration

set_network(Devnet)


def test_delegate_registration_transaction():
    """Test if a delegate registration transaction gets built
    """
    delegate_name = 'mr.delegate'

    transaction = DelegateRegistration(delegate_name)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.schnorr_sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['asset']['delegate']['username'] == delegate_name
    assert transaction_dict['type'] is TRANSACTION_DELEGATE_REGISTRATION
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 2500000000

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid


def test_delegate_registration_transaction_custom_fee():
    """Test if a delegate registration transaction gets built with a custom fee
    """
    delegate_name = 'mr.delegate'

    transaction = DelegateRegistration(delegate_name, 5)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.schnorr_sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['asset']['delegate']['username'] == delegate_name
    assert transaction_dict['type'] is TRANSACTION_DELEGATE_REGISTRATION
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 5

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid
