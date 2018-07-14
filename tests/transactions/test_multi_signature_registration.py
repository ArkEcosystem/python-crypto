from crypto.constants import TRANSACTION_MULTI_SIGNATURE_REGISTRATION
from crypto.transactions.multi_signature_registration import MultiSignatureRegistrationTransaction


def test_multi_signature_registration_transaction():
    """Test if a second signature registration transaction gets built
    """
    keysgroup = [
        '03a02b9d5fdd1307c2ee4652ba54d492d1fd11a7d1bb3f3a44c4a05e79f19de933',
        '13a02b9d5fdd1307c2ee4652ba54d492d1fd11a7d1bb3f3a44c4a05e79f19de933',
        '23a02b9d5fdd1307c2ee4652ba54d492d1fd11a7d1bb3f3a44c4a05e79f19de933',
    ]
    transaction = MultiSignatureRegistrationTransaction(2, 255, keysgroup)
    transaction.sign('secret'.encode())
    transaction.second_sign('second secret'.encode())
    transaction_dict = transaction.to_dict()
    assert transaction_dict['signature']
    assert transaction_dict['type'] is TRANSACTION_MULTI_SIGNATURE_REGISTRATION
