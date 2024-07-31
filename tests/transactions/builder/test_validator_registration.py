from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_VALIDATOR_REGISTRATION, TRANSACTION_TYPE_GROUP
from crypto.networks.devnet import Devnet
from crypto.transactions.builder.validator_registration import ValidatorRegistration

set_network(Devnet)


def test_validator_registration_transaction(passphrase):
    """Test if a validator registration transaction gets built
    """
    bls_public_key = 'b5fea88b9aab3f0b122e5a7e1b07917e62a63ea59103d0a0715ecded3c41685af88f0a9606309b148b3b50f51a2e7036'

    transaction = ValidatorRegistration(bls_public_key)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.sign(passphrase)
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['asset']['validatorPublicKey'] == bls_public_key
    assert transaction_dict['type'] is TRANSACTION_VALIDATOR_REGISTRATION
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 2500000000
    assert transaction_dict['expiration'] == 0
    assert transaction_dict['senderPublicKey'] == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid


def test_validator_registration_transaction_with_invalid_bls_public_key():
    """Test if a validator registration transaction fails with an invalid BLS public key
    """
    try:
        ValidatorRegistration('b5fea88b9aab3f0b122e5a7e1b07917e62a63ea59103d0a0715ecded3c41685af88f0a9606309b148b3b50f51a2edddd')

        raise Exception('ValidatorRegistration should raise an exception with an invalid BLS public key')
    except ValueError as e:
        assert e.args[0] == 'Invalid BLS public key'


def test_validator_registration_transaction_with_invalid_bls_public_key_by_length():
    """Test if a validator registration transaction fails with an invalid BLS public key
    """
    try:
        ValidatorRegistration('023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3')

        raise Exception('ValidatorRegistration should raise an exception with an invalid BLS public key')
    except ValueError as e:
        assert e.args[0] == 'Invalid BLS public key'


def test_validator_registration_transaction_custom_fee(passphrase):
    """Test if a validator registration transaction gets built with a custom fee
    """
    bls_public_key = 'b5fea88b9aab3f0b122e5a7e1b07917e62a63ea59103d0a0715ecded3c41685af88f0a9606309b148b3b50f51a2e7036'

    transaction = ValidatorRegistration(bls_public_key, 5)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.sign(passphrase)
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['asset']['validatorPublicKey'] == bls_public_key
    assert transaction_dict['type'] is TRANSACTION_VALIDATOR_REGISTRATION
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 5
    assert transaction_dict['expiration'] == 0
    assert transaction_dict['senderPublicKey'] == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid
