from crypto.configuration.fee import get_fee
from crypto.identity.public_key import PublicKey
from crypto.transactions.transaction import Transaction
from crypto.utils.message import Message


class BaseTransactionBuilder(object):

    def __init__(self):
        self.transaction = Transaction()
        self.transaction.type = getattr(self, 'transaction_type', None)
        self.transaction.fee = get_fee(getattr(self, 'transaction_type', None))

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
        message = Message.sign(self.transaction.to_bytes(), passphrase)
        self.transaction.signature = message.signature
        self.transaction.id = self.transaction.get_id()

    def second_sign(self, passphrase):
        """Sign the transaction using the given second passphrase

        Args:
            passphrase (str): 2nd passphrase associated with the account sending this transaction
        """
        message = Message.sign(self.transaction.to_bytes(skip_signature=False), passphrase)
        self.transaction.signSignature = message.signature
        self.transaction.id = self.transaction.get_id()

    def verify(self):
        self.transaction.verify()

    def second_verify(self):
        self.transaction.second_verify()
