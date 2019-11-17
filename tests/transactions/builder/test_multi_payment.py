from crypto.constants import TRANSACTION_MULTI_PAYMENT, TRANSACTION_TYPE_GROUP
from crypto.transactions.builder.multi_payment import MultiPayment


def test_multi_payment_transaction():
    """Test if multi payment transaction gets built
    """
    transaction = MultiPayment()
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(123)
    transaction.add_payment(1, 'AHXtmB84sTZ9Zd35h9Y1vfFvPE2Xzqj8ri')
    transaction.sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 123
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_MULTI_PAYMENT
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['asset']['payments'][0]['amount'] == 1
    assert transaction_dict['asset']['payments'][0]['recipientId'] == 'AHXtmB84sTZ9Zd35h9Y1vfFvPE2Xzqj8ri'

    transaction.verify()  # if no exception is raised, it means the transaction is valid
