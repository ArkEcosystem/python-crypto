from base58 import b58encode

from crypto.constants import TRANSACTION_IPFS, TRANSACTION_TYPE_GROUP
from crypto.transactions.builder.ipfs import IPFS


def test_ipfs_transaction():
    """Test if ipfs transaction gets built
    """
    ipfs_id = b58encode('hello')

    transaction = IPFS(ipfs_id)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(123)
    transaction.schnorr_sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 123
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_IPFS
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['asset']['ipfs'] == ipfs_id

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid
