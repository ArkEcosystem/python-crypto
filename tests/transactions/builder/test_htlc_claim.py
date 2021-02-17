from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_HTLC_CLAIM, TRANSACTION_TYPE_GROUP
from crypto.networks.devnet import Devnet
from crypto.transactions.builder.htlc_claim import HtlcClaim

set_network(Devnet)


def test_htlc_claim_transaction():
    """Test if timelock transaction gets built
    """
    lock_transaction_id = '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'

    # This should be the hashed secret used for HTLC Lock transaction
    unlock_secret = 'my secret that should be 32bytes'

    transaction = HtlcClaim(lock_transaction_id, unlock_secret)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.schnorr_sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_HTLC_CLAIM
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 0
    assert transaction_dict['asset']['claim']['lockTransactionId'] == '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'
    assert transaction_dict['asset']['claim']['unlockSecret'] == 'my secret that should be 32bytes'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid


def test_htlc_claim_transaction_custom_fee():
    """Test if timelock transaction gets built with a custom fee
    """
    lock_transaction_id = '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'

    # This should be the hashed secret used for HTLC Lock transaction
    unlock_secret = 'my secret that should be 32bytes'

    transaction = HtlcClaim(lock_transaction_id, unlock_secret, 5)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.schnorr_sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_HTLC_CLAIM
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 5
    assert transaction_dict['asset']['claim']['lockTransactionId'] == '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'
    assert transaction_dict['asset']['claim']['unlockSecret'] == 'my secret that should be 32bytes'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid
