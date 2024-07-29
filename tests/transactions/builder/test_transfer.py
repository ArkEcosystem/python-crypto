import pytest

from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_TRANSFER, TRANSACTION_TYPE_GROUP
from crypto.identity.public_key import PublicKey
from crypto.networks.devnet import Devnet
from crypto.transactions.builder.transfer import Transfer


set_network(Devnet)


def test_transfer_transaction(passphrase):
    """Test if a transfer transaction gets built
    """
    transaction = Transfer(
        recipientId='0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22',
        amount=1,
        fee=10000000,
        # timestamp=1720707047217,
    )
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(8)
    # transaction.transaction.id = '495afb812cb0ecfe7ac4d383b54d6458b53bb9be5ab37e2207bbd7ce82fdbc94'
    transaction.sign(passphrase)
    transaction_dict = transaction.to_dict()

    print(transaction_dict, transaction)

    assert transaction_dict['version'] == 1
    assert transaction_dict['nonce'] == 8
    assert transaction_dict['type'] is TRANSACTION_TRANSFER
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 10000000
    assert transaction_dict['amount'] == 1
    assert transaction_dict['expiration'] == 0
    assert transaction_dict['senderPublicKey'] == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid


def test_transfer_transaction_update_amount(passphrase):
    """Test if a transfer transaction can update an amount
    """
    transaction = Transfer(
        recipientId='0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22',
        amount=200000000
    )
    transaction.set_amount(10)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.sign(passphrase)
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_TRANSFER
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['amount'] == 10
    assert transaction_dict['expiration'] == 0
    assert transaction_dict['senderPublicKey'] == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid


def test_transfer_transaction_custom_fee(passphrase):
    """Test if a transfer transaction gets built with a custom fee
    """
    transaction = Transfer(
        recipientId='0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22',
        amount=200000000,
        fee=5
    )
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.sign(passphrase)
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_TRANSFER
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 5
    assert transaction_dict['expiration'] == 0
    assert transaction_dict['senderPublicKey'] == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid


def test_transfer_secondsign_transaction(passphrase):
    """Test if a transfer transaction with second signature gets built
    """
    transaction = Transfer(
        recipientId='0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22',
        amount=200000000,
    )
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.sign(passphrase)
    transaction.second_sign('second top secret passphrase')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['signSignature']
    assert transaction_dict['type'] is TRANSACTION_TRANSFER
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['expiration'] == 0
    assert transaction_dict['senderPublicKey'] == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid
    transaction.schnorr_verify_second(PublicKey.from_passphrase('second top secret passphrase'))  # if no exception is raised, it means the transaction is valid


def test_parse_signatures(transaction_type_0):
    """Test if parse signature works when parsing serialized data
    """
    transfer = Transfer(
        recipientId=transaction_type_0['recipientId'],
        amount=transaction_type_0['amount']
    )
    assert transfer.transaction.signature is None
    transfer.transaction.parse_signatures(transaction_type_0['serialized'], 166)
    assert transfer.transaction.signature


def test_transfer_transaction_amount_not_int():
    with pytest.raises(ValueError):
        """Test error handling in constructor for non-integer amount
        """
        Transfer(
            recipientId='0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22',
            amount='bad amount'
        )


def test_transfer_transaction_amount_zero():
    with pytest.raises(ValueError):
        """Test error handling in constructor for non-integer amount
        """
        Transfer(
            recipientId='0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22',
            amount=0
        )


def test_transfer_serialize(passphrase):
    transaction = Transfer(
        recipientId='0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22',
        amount=1,
        fee=10000000,
    )
    transaction.set_nonce(6)
    transaction.sign(passphrase)
    transaction.transaction.signature = '42faaaf6b5b5eff5bb78c7bb2b116ecbc0a83f53445b801818b72afb34b39226646608d5e7048c12d6aedcebfc3156f035b57ca70c6a5e899b7ac2a1be163bb0'

    assert transaction.serialize(False, False, False) == 'ff011e0100000000000600000000000000023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d38096980000000000000100000000000000000000006f0182a0cc707b055322ccf6d4cb6a5aff1aeb2242faaaf6b5b5eff5bb78c7bb2b116ecbc0a83f53445b801818b72afb34b39226646608d5e7048c12d6aedcebfc3156f035b57ca70c6a5e899b7ac2a1be163bb0'
