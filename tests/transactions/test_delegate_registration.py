from crypto.conf import use_network
from crypto.constants import TRANSACTION_DELEGATE_REGISTRATION
from crypto.transactions.delegate_registration import DelegateRegistrationTransaction


def test_delegate_registration_transaction():
    """Test if a delegate registration transaction gets built
    """
    use_network('devnet')
    delegate_name = 'mr.delegate'.encode()
    transaction = DelegateRegistrationTransaction(delegate_name)
    transaction.sign('testing'.encode())
    transaction_dict = transaction.to_dict()
    assert transaction_dict['signature']
    assert transaction_dict['asset']['delegate']['username'] == delegate_name
    assert transaction_dict['type'] is TRANSACTION_DELEGATE_REGISTRATION
