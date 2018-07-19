from crypto.conf import use_network
from crypto.constants import TRANSACTION_SECOND_SIGNATURE_REGISTRATION
from crypto.transactions.second_signature_registration import SecondSignatureRegistrationTransaction


def test_second_signature_registration_transaction():
    """Test if a second signature registration transaction gets built
    """
    use_network('devnet')
    transaction = SecondSignatureRegistrationTransaction('this is the second passphrase'.encode())
    transaction.sign('testing'.encode())
    transaction_dict = transaction.to_dict()
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_SECOND_SIGNATURE_REGISTRATION
    transaction.verify()  # if no exception is raised, it means the transaction is valid
