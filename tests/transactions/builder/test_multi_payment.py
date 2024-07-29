from crypto.configuration.network import set_network
from crypto.constants import TRANSACTION_MULTI_PAYMENT, TRANSACTION_TYPE_GROUP
from crypto.networks.devnet import Devnet
from crypto.transactions.builder.multi_payment import MultiPayment

set_network(Devnet)


def test_multi_payment_transaction(passphrase):
    """Test if multi payment transaction gets built
    """
    transaction = MultiPayment()
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.add_payment(1, '0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22')
    transaction.add_payment(2, '0xb693449AdDa7EFc015D87944EAE8b7C37EB1690A')
    transaction.sign(passphrase)
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_MULTI_PAYMENT
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 10000000
    assert transaction_dict['expiration'] == 0
    assert transaction_dict['senderPublicKey'] == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'

    assert transaction_dict['asset']['payments'][0]['amount'] == 1
    assert transaction_dict['asset']['payments'][0]['recipientId'] == '0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22'
    assert transaction_dict['asset']['payments'][1]['amount'] == 2
    assert transaction_dict['asset']['payments'][1]['recipientId'] == '0xb693449AdDa7EFc015D87944EAE8b7C37EB1690A'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid


def test_multi_payment_transaction_custom_fee(passphrase):
    """Test if multi payment transaction gets built with a custom fee
    """
    transaction = MultiPayment(fee=5)
    transaction.set_type_group(TRANSACTION_TYPE_GROUP.CORE)
    transaction.set_nonce(1)
    transaction.add_payment(1, '0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22')
    transaction.add_payment(2, '0xb693449AdDa7EFc015D87944EAE8b7C37EB1690A')
    transaction.sign(passphrase)
    transaction_dict = transaction.to_dict()

    assert transaction_dict['nonce'] == 1
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_MULTI_PAYMENT
    assert transaction_dict['typeGroup'] == 1
    assert transaction_dict['typeGroup'] == TRANSACTION_TYPE_GROUP.CORE.value
    assert transaction_dict['fee'] == 5
    assert transaction_dict['expiration'] == 0
    assert transaction_dict['senderPublicKey'] == '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'

    assert transaction_dict['asset']['payments'][0]['amount'] == 1
    assert transaction_dict['asset']['payments'][0]['recipientId'] == '0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22'
    assert transaction_dict['asset']['payments'][1]['amount'] == 2
    assert transaction_dict['asset']['payments'][1]['recipientId'] == '0xb693449AdDa7EFc015D87944EAE8b7C37EB1690A'

    transaction.schnorr_verify()  # if no exception is raised, it means the transaction is valid
