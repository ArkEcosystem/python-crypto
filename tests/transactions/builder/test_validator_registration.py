from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_VALIDATOR_REGISTRATION, TRANSACTION_TYPE_GROUP
from crypto.networks.devnet import Devnet
from crypto.transactions.builder.validator_registration import ValidatorRegistration

set_network(Devnet)


def test_validator_registration_transaction(passphrase):
    """Test if a validator registration transaction gets built
    """
    bls_public_key = 'a227bf7c57eaa6e4f5de7b17495b4ea0be645d1204ce2fc9b54dbfabe23a59b6377e924c12aa4a831483af021fbc29ec'

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


def test_validator_registration_transaction_custom_fee(passphrase):
    """Test if a validator registration transaction gets built with a custom fee
    """
    bls_public_key = 'a227bf7c57eaa6e4f5de7b17495b4ea0be645d1204ce2fc9b54dbfabe23a59b6377e924c12aa4a831483af021fbc29ec'

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
