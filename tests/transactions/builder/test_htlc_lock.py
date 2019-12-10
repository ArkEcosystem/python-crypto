from crypto.constants import TRANSACTION_HTLC_LOCK, TRANSACTION_TYPE_GROUP
from crypto.transactions.builder.htlc_lock import HtlcLock


def test_htlc_lock_transaction():
    """Test if timelock transaction gets built
    """
    transaction = HtlcLock(
      recipient_id='AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC',
      secret_hash='0f128d401958b1b30ad0d10406f47f9489321017b4614e6cb993fc63913c5454',
      expiration_type=1,
      expiration_value=1573455822
    )

    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(123)
    transaction.schnorr_sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['recipientId'] == 'AGeYmgbg2LgGxRW2vNNJvQ88PknEJsYizC'
    assert transaction_dict['nonce'] == 123
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_HTLC_LOCK
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['asset']['lock']['secretHash'] == '0f128d401958b1b30ad0d10406f47f9489321017b4614e6cb993fc63913c5454'
    assert transaction_dict['asset']['lock']['expiration']['type'] == 1
    assert transaction_dict['asset']['lock']['expiration']['value'] == 1573455822

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid
