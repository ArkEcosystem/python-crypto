from crypto.exceptions import InvalidUsernameException
from crypto.transactions.builder.username_registration_builder import UsernameRegistrationBuilder

def test_username_registration_transaction(passphrase, username, load_transaction_fixture):
    fixture = load_transaction_fixture('username-registration')

    builder = (
        UsernameRegistrationBuilder
            .new()
            .gas_price(fixture['data']['gasPrice'])
            .nonce(fixture['data']['nonce'])
            .network(fixture['data']['network'])
            .gas_limit(fixture['data']['gasLimit'])
            .username(username)
            .sign(passphrase)
    )

    assert builder.transaction.serialize().hex() == fixture['serialized']
    assert builder.transaction.data['id'] == fixture['data']['id']
    assert builder.verify()

def test_it_accepts_valid_usernames():
    try:
        UsernameRegistrationBuilder.is_valid_username('john')
        UsernameRegistrationBuilder.is_valid_username('john123')
        UsernameRegistrationBuilder.is_valid_username('john_doe')
        UsernameRegistrationBuilder.is_valid_username('a')
        UsernameRegistrationBuilder.is_valid_username('abcdefghijklmnopqrst')
        UsernameRegistrationBuilder.is_valid_username('user_123_name')
    except InvalidUsernameException as e:
        raise Exception(f'Valid username threw an exception: {e}')

def test_it_rejects_usernames_with_invalid_length():
    for username, character_count in {'': 0, 'abcdefghijklmnopqrstu': 21}.items():
        try:
            UsernameRegistrationBuilder.is_valid_username(username)
        except InvalidUsernameException as e:
            assert str(e) == f'Username must be between 1 and 20 characters long. Got {character_count} characters.'

def test_it_rejects_usernames_with_invalid_characters():
    usernames = [
        'John',
        'john@doe',
        'john doe',
        'jöhn',
    ]

    for username in usernames:
        try:
            UsernameRegistrationBuilder.is_valid_username(username)
        except InvalidUsernameException as e:
            assert str(e) == 'Username can only contain lowercase letters, numbers and underscores'

def test_it_rejects_usernames_starting_or_ending_with_underscore():
    usernames = [
        '_john',
        'john_',
        '_john_',
    ]

    for username in usernames:
        try:
            UsernameRegistrationBuilder.is_valid_username(username)
        except InvalidUsernameException as e:
            assert str(e) == 'Username cannot start or end with an underscore'

def test_it_rejects_usernames_with_consecutive_underscores():
    usernames = [
        'john__doe',
        'john___doe',
        'john__doe__smith',
    ]

    for username in usernames:
        try:
            UsernameRegistrationBuilder.is_valid_username(username)
        except InvalidUsernameException as e:
            assert str(e) == 'Username cannot contain consecutive underscores'
