from crypto.constants import TRANSACTION_TRANSFER, TRANSACTION_TYPE_GROUP
from crypto.transactions.builder.transfer import Transfer


def test_transfer_transaction():
    """Test if a transfer transaction gets built
    """
    transaction = Transfer(
        recipientId='AXoXnFi4z1Z6aFvjEYkDVCtBGW2PaRiM25',
        amount=1000,
        vendorField='Hello Pythonistas!'
    )
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(123)
    transaction.sign('This is a top secret passphrase')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 123
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_TRANSFER
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value

    transaction.verify()  # if no exception is raised, it means the transaction is valid


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
