from crypto.constants import TRANSACTION_DELEGATE_REGISTRATION
from crypto.transactions.builder.delegate_registration import DelegateRegistrationTransaction


def test_delegate_registration_transaction():
    """Test if a delegate registration transaction gets built
    """
    delegate_name = 'mr.delegate'
    transaction = DelegateRegistrationTransaction(delegate_name)
    transaction.sign('testing')
    transaction_dict = transaction.to_dict()
    assert transaction_dict['signature']
    assert transaction_dict['asset']['delegate']['username'] == delegate_name
    assert transaction_dict['type'] is TRANSACTION_DELEGATE_REGISTRATION
    transaction.verify()  # if no exception is raised, it means the transaction is valid
