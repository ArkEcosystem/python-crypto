import pytest

from crypto.enums.contract_addresses import ContractAddresses
from crypto.transactions.builder.batch_transfer_builder import (
    BatchTransferBuilder,
)

RECIPIENT_A = '0x6F0182a0cc707b055322CcF6d4CB6a5Aff1aEb22'
RECIPIENT_B = '0xc3bbe9b1cee1ff85ad72b87414b0e9b7f2366763'
TOKEN_ADDRESS = '0xdAC17F958D2ee523a2206206994597C13D831ec7'


def test_it_should_default_to_the_batch_transfer_contract():
    builder = BatchTransferBuilder.new()

    assert builder.transaction.data['to'] == ContractAddresses.BATCH_TRANSFER.value


def test_it_should_sign_it_with_a_passphrase(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/batch-transfer')

    builder = (
        BatchTransferBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .gas_limit(fixture['data']['gasLimit'])
            .nonce(fixture['data']['nonce'])
            .token_address(TOKEN_ADDRESS)
            .add_recipient(RECIPIENT_A, 100000)
            .add_recipient(RECIPIENT_B, 200000)
            .sign(passphrase)
    )

    assert builder.transaction.data['gasPrice'] == int(fixture['data']['gasPrice'])
    assert builder.transaction.data['gasLimit'] == int(fixture['data']['gasLimit'])
    assert builder.transaction.data['nonce'] == fixture['data']['nonce']
    assert builder.transaction.data['value'] == 0
    assert builder.transaction.data['to'] == fixture['data']['to']
    assert builder.transaction.data['data'] == fixture['data']['data']
    assert builder.transaction.data['v'] == fixture['data']['v']
    assert builder.transaction.data['r'] == fixture['data']['r']
    assert builder.transaction.data['s'] == fixture['data']['s']
    assert builder.transaction.data['hash'] == fixture['data']['hash']

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.verify()


def test_it_should_handle_single_recipient(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/batch-transfer')

    builder = (
        BatchTransferBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .gas_limit(fixture['data']['gasLimit'])
            .nonce(fixture['data']['nonce'])
            .token_address(TOKEN_ADDRESS)
            .add_recipient(RECIPIENT_A, 100000)
            .sign(passphrase)
    )

    assert builder.transaction.data['data'].startswith('4885b254')
    assert builder.transaction.data['value'] == 0
    assert builder.verify()


def test_it_should_encode_large_amounts(passphrase, load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/batch-transfer')

    builder = (
        BatchTransferBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .gas_limit(fixture['data']['gasLimit'])
            .nonce(fixture['data']['nonce'])
            .token_address(TOKEN_ADDRESS)
            .add_recipient(RECIPIENT_A, 1000000000000000000000)
            .sign(passphrase)
    )

    assert builder.verify()


def test_it_should_throw_when_signing_with_no_recipients(passphrase):
    builder = (
        BatchTransferBuilder
            .new()
            .gas_price('5000000000')
            .gas_limit('21000')
            .nonce('1')
            .token_address(TOKEN_ADDRESS)
    )

    with pytest.raises(Exception, match='Must add at least one recipient before encoding.'):
        builder.sign(passphrase)


def test_it_should_throw_when_signing_without_a_token_address(passphrase):
    builder = (
        BatchTransferBuilder
            .new()
            .gas_price('5000000000')
            .gas_limit('21000')
            .nonce('1')
            .add_recipient(RECIPIENT_A, 100000)
    )

    with pytest.raises(Exception, match='Must set tokenAddress before encoding.'):
        builder.sign(passphrase)
