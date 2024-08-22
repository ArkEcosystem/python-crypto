from crypto.constants import TRANSACTION_FEES
from crypto.identity.public_key import PublicKey
from crypto.transactions.builder.multi_signature_registration import MultiSignatureRegistration
from crypto.transactions.deserializer import Deserializer
from crypto.transactions.serializer import Serializer


def test_multi_signature_registration_deserializer(transaction_type_4):
    deserializer = Deserializer(transaction_type_4['serialized'])
    actual = deserializer.deserialize()

    assert actual.version == transaction_type_4['version']
    assert actual.network == transaction_type_4['network']
    assert actual.typeGroup == transaction_type_4['typeGroup']
    assert actual.type == transaction_type_4['type']
    assert actual.nonce == transaction_type_4['nonce']
    assert actual.senderPublicKey == transaction_type_4['senderPublicKey']
    assert actual.fee == transaction_type_4['fee']
    assert actual.amount == transaction_type_4['amount']
    assert actual.signature == transaction_type_4['signature']
    assert actual.id == transaction_type_4['id']

    assert actual.asset['multiSignature']['min'] == transaction_type_4['asset']['multiSignature']['min']
    assert actual.asset['multiSignature']['publicKeys'] == transaction_type_4['asset']['multiSignature']['publicKeys']
    assert actual.signatures == transaction_type_4['signatures']

    actual.verify_multisig_schnorr()


def test_multi_signature_registration_deserializer_from_serialized(transaction_type_4):
    result = Serializer(transaction_type_4).serialize(False, True, False)

    deserializer = Deserializer(result)
    actual = deserializer.deserialize()

    assert actual.version == transaction_type_4['version']
    assert actual.network == transaction_type_4['network']
    assert actual.typeGroup == transaction_type_4['typeGroup']
    assert actual.type == transaction_type_4['type']
    assert actual.nonce == transaction_type_4['nonce']
    assert actual.senderPublicKey == transaction_type_4['senderPublicKey']
    assert actual.fee == transaction_type_4['fee']
    assert actual.amount == transaction_type_4['amount']
    assert actual.signature == transaction_type_4['signature']
    assert actual.id == transaction_type_4['id']

    assert actual.asset['multiSignature']['min'] == transaction_type_4['asset']['multiSignature']['min']
    assert actual.asset['multiSignature']['publicKeys'] == transaction_type_4['asset']['multiSignature']['publicKeys']
    assert actual.signatures == transaction_type_4['signatures']

    actual.verify_multisig_schnorr()

def test_with_methods(passphrase):
    transaction = MultiSignatureRegistration()

    passphrase_2 = f'{passphrase} 2'
    passphrase_3 = f'{passphrase} 3'

    sender_public_key = PublicKey.from_passphrase(passphrase)
    participant_2 = PublicKey.from_passphrase(passphrase_2)
    participant_3 = PublicKey.from_passphrase(passphrase_3)

    transaction.set_sender_public_key(sender_public_key)
    transaction.set_nonce(15)
    transaction.set_min(2)
    transaction.add_participant(sender_public_key)
    transaction.add_participant(participant_2)
    transaction.add_participant(participant_3)

    transaction.multi_sign(passphrase, 0)
    transaction.multi_sign(passphrase_2, 1)
    transaction.multi_sign(passphrase_3, 2)

    transaction.sign(passphrase)

    result = Serializer(transaction.to_dict()).serialize(False, True, False)

    deserializer = Deserializer(result)
    actual = deserializer.deserialize()

    assert actual.version == 1
    assert actual.network == 30
    assert actual.typeGroup == 1
    assert actual.type == 4
    assert actual.nonce == 15
    assert actual.senderPublicKey == sender_public_key
    assert actual.fee == TRANSACTION_FEES[4] * 4
    assert actual.amount == 0
    assert actual.signature == transaction.transaction.signature
    assert actual.id == transaction.transaction.id

    assert actual.asset['multiSignature']['min'] == 2
    assert actual.asset['multiSignature']['publicKeys'][0] == sender_public_key
    assert actual.asset['multiSignature']['publicKeys'][1] == participant_2
    assert actual.asset['multiSignature']['publicKeys'][2] == participant_3

    assert actual.signatures == transaction.transaction.signatures
    assert len(actual.signatures) == 3

    actual.verify_multisig_schnorr()
