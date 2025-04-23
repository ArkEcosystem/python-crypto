import re
from crypto.enums.contract_addresses import ContractAddresses
from crypto.exceptions import InvalidUsernameException
from crypto.transactions.builder.abstract_transaction_builder import AbstractTransactionBuilder
from crypto.transactions.types.username_registration import UsernameRegistration

class UsernameRegistrationBuilder(AbstractTransactionBuilder):
    def __init__(self, data: dict):
        super().__init__(data)

        self.recipient_address(ContractAddresses.USERNAMES.value)

    def username(self, username: str):
        self.is_valid_username(username)

        self.transaction.data['username'] = username
        self.transaction.refresh_payload_data()

        return self

    def get_transaction_instance(self, data: dict):
        return UsernameRegistration(data)

    @staticmethod
    def is_valid_username(username: str) -> bool:
        if len(username) < 1 or len(username) > 20:
            raise InvalidUsernameException(f'Username must be between 1 and 20 characters long. Got {len(username)} characters.')

        if re.match('/[^a-z0-9_]/', username):
            raise InvalidUsernameException('Username can only contain lowercase letters, numbers and underscores.')

        if re.match('/^_|_$/', username):
            raise InvalidUsernameException('Username cannot start or end with an underscore.')

        if re.match('/__/', username):
            raise InvalidUsernameException('Username cannot contain consecutive underscores.')

        return True
