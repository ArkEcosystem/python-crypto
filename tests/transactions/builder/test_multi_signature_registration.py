from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_MULTI_SIGNATURE_REGISTRATION, TRANSACTION_TYPE_GROUP
from crypto.networks.devnet import Devnet
from crypto.transactions.builder.multi_signature_registration import MultiSignatureRegistration

set_network(Devnet)


def test_multi_signature_registration_transaction():
    """Test if a second signature registration transaction gets built
    """
    publicKeys = [
        '0205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b896',
        '03df0a1eb42d99b5de395cead145ba1ec2ea837be308c7ce3a4e8018b7efc7fdb8',
    ]

    transaction = MultiSignatureRegistration()
    transaction.set_sender_public_key('0205d9bbe71c343ac9a6a83a4344fd404c3534fc7349827097d0835d160bc2b896')
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.set_min(2)
    transaction.set_public_keys(publicKeys)
    transaction.add_participant('03860d76b1df09659ac282cea3da5bd84fc45729f348a4a8e5f802186be72dc17f')
    transaction.multi_sign('this is a top secret passphrase 1', 0)
    transaction.multi_sign('this is a top secret passphrase 2', 1)
    transaction.multi_sign('this is a top secret passphrase 3', 2)

    transaction.schnorr_sign('this is a top secret passphrase 1')

    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['version'] == 2
    assert transaction_dict['fee'] == 2000000000
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_MULTI_SIGNATURE_REGISTRATION
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['asset']['multiSignature']['min'] == 2

    assert transaction_dict['asset']['multiSignature']['publicKeys'][0] == publicKeys[0]
    assert transaction_dict['asset']['multiSignature']['publicKeys'][1] == publicKeys[1]
    assert transaction_dict['asset']['multiSignature']['publicKeys'][2] == '03860d76b1df09659ac282cea3da5bd84fc45729f348a4a8e5f802186be72dc17f'

    transaction.schnorr_verify_multisig()  # if no exception is raised, it means the transaction is valid
