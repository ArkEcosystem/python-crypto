from crypto.constants import TRANSACTION_DELEGATE_RESIGNATION, TRANSACTION_TYPE_GROUP
from crypto.transactions.builder.delegate_resignation import DelegateResignation


def test_delegate_resignation_transaction():
    """Test if delegate resignation transaction gets built
    """
    transaction = DelegateResignation()
    transaction.set_nonce(1)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.schnorr_sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_DELEGATE_RESIGNATION
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid
