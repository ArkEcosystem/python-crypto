from crypto.constants import TRANSACTION_TIMELOCK_CLAIM, TRANSACTION_TYPE_GROUP
from crypto.transactions.builder.timelock_claim import TimelockClaim

def test_timelock_claim_transaction():
    """Test if timelock transaction gets built
    """
    lock_transaction_id = '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'
    # @TODO: Not sure here, shouldn't the builder take a bytes encoded string instead of accepting a plain string ?
    unlock_secret = 'my secret that should be 32bytes'
    transaction = TimelockClaim(lock_transaction_id, unlock_secret)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(123)
    transaction.sign('testing')
    transaction_dict = transaction.to_dict()
    assert transaction_dict['nonce'] == 123
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_TIMELOCK_CLAIM
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['asset']['claim']['lockTransactionId'] == '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'
    assert transaction_dict['asset']['claim']['unlockSecret'] == 'my secret that should be 32bytes'
    transaction.verify()  # if no exception is raised, it means the transaction is valid
