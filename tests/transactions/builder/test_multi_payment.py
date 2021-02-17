from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_MULTI_PAYMENT, TRANSACTION_TYPE_GROUP
from crypto.networks.devnet import Devnet
from crypto.transactions.builder.multi_payment import MultiPayment

set_network(Devnet)


def test_multi_payment_transaction():
    """Test if multi payment transaction gets built
    """
    transaction = MultiPayment()
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.add_payment(1, 'AHXtmB84sTZ9Zd35h9Y1vfFvPE2Xzqj8ri')
    transaction.add_payment(2, 'ATK14wxyYxbELq2b91bAfBY8Vmh9J6MDej')
    transaction.schnorr_sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_MULTI_PAYMENT
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 10000000
    assert transaction_dict['asset']['payments'][0]['amount'] == 1
    assert transaction_dict['asset']['payments'][0]['recipientId'] == 'AHXtmB84sTZ9Zd35h9Y1vfFvPE2Xzqj8ri'
    assert transaction_dict['asset']['payments'][1]['amount'] == 2
    assert transaction_dict['asset']['payments'][1]['recipientId'] == 'ATK14wxyYxbELq2b91bAfBY8Vmh9J6MDej'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid


def test_multi_payment_transaction_custom_fee():
    """Test if multi payment transaction gets built with a custom fee
    """
    transaction = MultiPayment(fee=5)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.add_payment(1, 'AHXtmB84sTZ9Zd35h9Y1vfFvPE2Xzqj8ri')
    transaction.add_payment(2, 'ATK14wxyYxbELq2b91bAfBY8Vmh9J6MDej')
    transaction.schnorr_sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_MULTI_PAYMENT
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 5
    assert transaction_dict['asset']['payments'][0]['amount'] == 1
    assert transaction_dict['asset']['payments'][0]['recipientId'] == 'AHXtmB84sTZ9Zd35h9Y1vfFvPE2Xzqj8ri'
    assert transaction_dict['asset']['payments'][1]['amount'] == 2
    assert transaction_dict['asset']['payments'][1]['recipientId'] == 'ATK14wxyYxbELq2b91bAfBY8Vmh9J6MDej'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid
