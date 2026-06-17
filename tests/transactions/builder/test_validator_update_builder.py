from crypto.enums.contract_addresses import ContractAddresses
from crypto.identity.proof_of_possession import ProofOfPossession
from crypto.transactions.builder.validator_update_builder import ValidatorUpdateBuilder


def test_validator_update_derives_bls_keys(passphrase, validator_passphrase):
    builder = (
        ValidatorUpdateBuilder
            .new()
            .gas_price(5000000000)
            .gas_limit(200000)
            .nonce('1')
            .validator_passphrase(validator_passphrase)
            .sign(passphrase)
    )

    bls = ProofOfPossession.from_passphrase(validator_passphrase)

    assert builder.transaction.data['validatorPublicKey'] == '0x' + bls['pk']
    assert builder.transaction.data['validatorProof']     == '0x' + bls['pop']
    assert len(builder.transaction.data['validatorPublicKey']) == 98   # 0x + 96 hex = 48 bytes
    assert len(builder.transaction.data['validatorProof'])     == 194  # 0x + 192 hex = 96 bytes


def test_validator_update_targets_consensus_contract(passphrase, validator_passphrase):
    builder = (
        ValidatorUpdateBuilder
            .new()
            .validator_passphrase(validator_passphrase)
            .sign(passphrase)
    )

    assert builder.transaction.data['to'].lower() == ContractAddresses.CONSENSUS.value.lower()


def test_validator_update_value_is_zero(passphrase, validator_passphrase):
    builder = (
        ValidatorUpdateBuilder
            .new()
            .validator_passphrase(validator_passphrase)
            .sign(passphrase)
    )

    assert builder.transaction.data['value'] == 0


def test_validator_update_verifies(passphrase, validator_passphrase):
    builder = (
        ValidatorUpdateBuilder
            .new()
            .validator_passphrase(validator_passphrase)
            .sign(passphrase)
    )

    assert builder.verify()
