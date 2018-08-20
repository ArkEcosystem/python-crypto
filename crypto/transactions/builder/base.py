from hashlib import sha256

from crypto.identity.public_key import PublicKey
from crypto.message import sign_message
from crypto.resources.transaction import Transaction


class BaseTransactionBuilder(object):

    def __init__(self):
        self.transaction = Transaction()
        self.transaction.type = getattr(self, 'transaction_type', None)

    def to_dict(self):
        return self.transaction.to_dict()

    def to_json(self):
        return self.transaction.to_json()

    def sign(self, passphrase):
        """Sign the transaction using the given passphrase

        Args:
            passphrase (str): passphrase associated with the account sending this transaction
        """
        self.transaction.senderPublicKey = PublicKey.from_passphrase(passphrase)
        message = sign_message(self.transaction.to_bytes(), passphrase)
        self.transaction.signature = message['signature']
        self.transaction.id = self.transaction.get_id()

    def second_sign(self, passphrase):
        """Sign the transaction using the given second passphrase

        Args:
            passphrase (str): 2nd passphrase associated with the account sending this transaction
        """
        transaction = sha256(self.transaction.to_bytes()).digest()
        message = sign_message(transaction, passphrase)
        self.transaction.signSignature = message['signature']
        self.transaction.id = self.transaction.get_id()

    def verify(self):
        self.transaction.verify()

    def second_verify(self):
        self.transaction.second_verify()
