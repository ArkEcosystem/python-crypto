from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_HTLC_REFUND, TRANSACTION_TYPE_GROUP
from crypto.networks.devnet import Devnet
from crypto.transactions.builder.htlc_refund import HtlcRefund

set_network(Devnet)


def test_timelock_refund_transaction():
    """Test if timelock transaction gets built
    """
    transaction = HtlcRefund(
      lock_transaction_id='943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'
    )

    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.schnorr_sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_HTLC_REFUND
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 0
    assert transaction_dict['asset']['refund']['lockTransactionId'] == '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid


def test_timelock_refund_transaction_custom_fee():
    """Test if timelock transaction gets built with custom fee
    """
    transaction = HtlcRefund(
      lock_transaction_id='943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4',
      fee=5
    )

    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.schnorr_sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_HTLC_REFUND
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 5
    assert transaction_dict['asset']['refund']['lockTransactionId'] == '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid
