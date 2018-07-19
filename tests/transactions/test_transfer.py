from crypto.conf import use_network
from crypto.constants import TRANSACTION_TRANSFER
from crypto.transactions.transfer import TransferTransaction


def test_transfer_transaction():
    """Test if a transfer transaction gets built
    """
    use_network('devnet')
    transaction = TransferTransaction(
        recipient_id='AXoXnFi4z1Z6aFvjEYkDVCtBGW2PaRiM25',
        amount=133380000000,
        vendor_field='This is a transaction from Python'.encode(),
    )
    transaction.sign('This is a top secret passphrase'.encode())
    transaction_dict = transaction.to_dict()
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_TRANSFER
    transaction.verify()  # if no exception is raised, it means the transaction is valid
