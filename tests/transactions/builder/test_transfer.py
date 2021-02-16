import pytest

from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_TRANSFER, TRANSACTION_TYPE_GROUP
from crypto.identity.public_key import PublicKey
from crypto.networks.devnet import Devnet
from crypto.transactions.builder.transfer import Transfer


set_network(Devnet)


def test_transfer_transaction():
    """Test if a transfer transaction gets built
    """
    transaction = Transfer(
        recipientId='AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC',
        amount=200000000,
    )
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.schnorr_sign('this is a top secret passphrase')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_TRANSFER
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 10000000

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid


def test_transfer_transaction_update_amount():
    """Test if a transfer transaction can update an amount
    """
    transaction = Transfer(
        recipientId='AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC',
        amount=200000000
    )
    transaction.set_amount(10)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.schnorr_sign('this is a top secret passphrase')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_TRANSFER
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['amount'] == 10

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid


def test_transfer_transaction_custom_fee():
    """Test if a transfer transaction gets built with a custom fee
    """
    transaction = Transfer(
        recipientId='AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC',
        amount=200000000,
        fee=5
    )
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.schnorr_sign('this is a top secret passphrase')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_TRANSFER
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 5

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid


def test_transfer_secondsig_transaction():
    """Test if a transfer transaction with second signature gets built
    """
    transaction = Transfer(
        recipientId='AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC',
        amount=200000000,
    )
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.schnorr_sign('this is a top secret passphrase')
    transaction.second_sign('second top secret passphrase')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['signSignature']
    assert transaction_dict['type'] is TRANSACTION_TRANSFER
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value

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
            recipientId='AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC',
            amount='bad amount'
        )


def test_transfer_transaction_amount_zero():
    with pytest.raises(ValueError):
        """Test error handling in constructor for non-integer amount
        """
        Transfer(
            recipientId='AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC',
            amount=0
        )
