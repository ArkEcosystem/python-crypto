from crypto.constants import TRANSACTION_TRANSFER, TRANSACTION_TYPE_GROUP
from crypto.transactions.builder.transfer import Transfer
from crypto.schnorr import schnorr


def test_transfer_transaction():
    """Test if a transfer transaction gets built
    """
    transaction = Transfer(
        recipientId='AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC',
        amount=200000000,
    )
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_version(2)
    transaction.set_network(23)
    transaction.schnorr_sign('this is a top secret passphrase')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_TRANSFER
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid


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
