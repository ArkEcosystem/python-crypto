from crypto.constants import TRANSACTION_SECOND_SIGNATURE_REGISTRATION
from crypto.transactions.builder.second_signature_registration import SecondSignatureRegistration


def test_second_signature_registration_transaction():
    """Test if a second signature registration transaction gets built
    """
    transaction = SecondSignatureRegistration('this is the second passphrase')
    transaction.sign('testing')
    transaction_dict = transaction.to_dict()
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_SECOND_SIGNATURE_REGISTRATION
    transaction.verify()  # if no exception is raised, it means the transaction is valid
