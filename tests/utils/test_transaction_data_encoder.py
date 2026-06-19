from crypto.utils.transaction_data_encoder import TransactionDataEncoder


def test_encode_token_transfer(load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/transaction-data-encoder')
    encoded = TransactionDataEncoder.token_transfer(
        fixture['Address'], fixture['Amount']
    )
    assert encoded == fixture['Encoded']['TokenTransfer']


def test_encode_username_registration(load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/transaction-data-encoder')
    encoded = TransactionDataEncoder.username_registration(fixture['Username'])
    assert encoded == fixture['Encoded']['UsernameRegistration']


def test_encode_username_resignation(load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/transaction-data-encoder')
    encoded = TransactionDataEncoder.username_resignation()
    assert encoded == fixture['Encoded']['UsernameResignation']


def test_encode_validator_registration(load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/transaction-data-encoder')
    encoded = TransactionDataEncoder.validator_registration(
        fixture['ValidatorPassphrase']
    )
    assert encoded == fixture['Encoded']['ValidatorRegistration']


def test_encode_update_validator(load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/transaction-data-encoder')
    encoded = TransactionDataEncoder.update_validator(
        fixture['ValidatorPassphrase']
    )
    assert encoded == fixture['Encoded']['UpdateValidator']


def test_encode_validator_resignation(load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/transaction-data-encoder')
    encoded = TransactionDataEncoder.validator_resignation()
    assert encoded == fixture['Encoded']['ValidatorResignation']


def test_encode_multi_payment(load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/transaction-data-encoder')
    encoded = TransactionDataEncoder.multi_payment(
        [fixture['Address']], ['1000']
    )
    assert encoded == fixture['Encoded']['MultiPayment']
