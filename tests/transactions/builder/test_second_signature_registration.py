from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_SECOND_SIGNATURE_REGISTRATION, TRANSACTION_TYPE_GROUP
from crypto.networks.devnet import Devnet
from crypto.transactions.builder.second_signature_registration import SecondSignatureRegistration

set_network(Devnet)


def test_second_signature_registration_transaction(passphrase):
    """Test if a second signature registration transaction gets built
    """
    transaction = SecondSignatureRegistration('this is a top secret passphrase')
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.sign(passphrase)
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_SECOND_SIGNATURE_REGISTRATION
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 500000000
    assert transaction_dict['expiration'] == 0
    assert transaction_dict['senderPublicKey'] == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid


def test_second_signature_registration_transaction_custom_fee(passphrase):
    """Test if a second signature registration transaction gets built with a custom fee
    """
    transaction = SecondSignatureRegistration('this is a top secret passphrase', 5)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.sign(passphrase)
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_SECOND_SIGNATURE_REGISTRATION
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 5
    assert transaction_dict['expiration'] == 0
    assert transaction_dict['senderPublicKey'] == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid
