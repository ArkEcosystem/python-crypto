from crypto.constants import TRANSACTION_SECOND_SIGNATURE_REGISTRATION, TRANSACTION_TYPE_GROUP
from crypto.transactions.builder.second_signature_registration import SecondSignatureRegistration


def test_second_signature_registration_transaction():
    """Test if a second signature registration transaction gets built
    """
    transaction = SecondSignatureRegistration('this is the second passphrase')
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.schnorr_sign('testing')
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_SECOND_SIGNATURE_REGISTRATION
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid
