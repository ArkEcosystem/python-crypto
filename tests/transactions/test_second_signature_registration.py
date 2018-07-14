from crypto.constants import TRANSACTION_SECOND_SIGNATURE_REGISTRATION
from crypto.transactions.second_signature_registration import SecondSignatureRegistrationTransaction


def test_second_signature_registration_transaction():
    """Test if a second signature registration transaction gets built
    """
    transaction = SecondSignatureRegistrationTransaction('this is the second passphrase'.encode())
    transaction.sign('testing'.encode())
    transaction_dict = transaction.to_dict()
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_SECOND_SIGNATURE_REGISTRATION
