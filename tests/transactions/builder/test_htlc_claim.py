import binascii
import pytest
from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_HTLC_CLAIM, TRANSACTION_TYPE_GROUP
from crypto.networks.devnet import Devnet
from crypto.exceptions import ArkSerializerException
from crypto.transactions.builder.htlc_claim import HtlcClaim

set_network(Devnet)


def test_htlc_claim_transaction_ok():
    """Test if timelock transaction gets built
    """
    lock_transaction_id = '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'

    # Secret required to unlock and claim funds from an HTLC. This secret should is revealed to you
    # on the blockchain which you can then use to claim funds.
    unlock_secret = '6434323233626639336532303235303561366135303134323161383864396661'

    transaction = HtlcClaim(lock_transaction_id, unlock_secret)
    transaction.set_nonce(1)
    transaction.schnorr_sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_HTLC_CLAIM
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 0
    assert transaction_dict['asset']['claim']['lockTransactionId'] == '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'
    assert transaction_dict['asset']['claim']['unlockSecret'] == unlock_secret

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid


def test_htlc_claim_transaction_unlock_secret_not_hex():
    """Test if timelock transaction errors if an invalid hex unlock_secret is given 
    """
    lock_transaction_id = '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'

    # Secret required to unlock and claim funds from an HTLC. This secret should is revealed to you
    # on the blockchain which you can then use to claim funds.
    unlock_secret = '643432323362663933653230323530356136613530313432316138a84a3966x1'

    transaction = HtlcClaim(lock_transaction_id, unlock_secret)
    transaction.set_nonce(1)
    with pytest.raises(binascii.Error) as e:
        transaction.schnorr_sign('testing')
    assert str(e.value) == 'Non-hexadecimal digit found'
   

def test_htlc_claim_transaction_unlock_secret_bad_length():
    """Test if timelock transaction fails if the unlock_secret is too big
    """
    lock_transaction_id = '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'

    # Secret required to unlock and claim funds from an HTLC. This secret should is revealed to you
    # on the blockchain which you can then use to claim funds.
    unlock_secret = '326632383634643861626534336530363236363132643461636235623535666462'

    transaction = HtlcClaim(lock_transaction_id, unlock_secret)
    transaction.set_nonce(1)
    with pytest.raises(ArkSerializerException) as e:
        transaction.schnorr_sign('testing')
    assert str(e.value) == 'Unlock secret must be 32 bytes long'


def test_htlc_claim_transaction_custom_fee_ok():
    """Test if timelock transaction gets built with a custom fee
    """
    lock_transaction_id = '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'

    # Secret required to unlock and claim funds from an HTLC. This secret should is revealed to you
    # on the blockchain which you can then use to claim funds.
    unlock_secret = '6434323233626639336532303235303561366135303134323161383864396661'

    transaction = HtlcClaim(lock_transaction_id, unlock_secret, 5)
    transaction.set_nonce(1)
    transaction.schnorr_sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_HTLC_CLAIM
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 5
    assert transaction_dict['asset']['claim']['lockTransactionId'] == '943c220691e711c39c79d437ce185748a0018940e1a4144293af9d05627d2eb4'
    assert transaction_dict['asset']['claim']['unlockSecret'] == unlock_secret

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid
