from binascii import hexlify, unhexlify

from crypto.configuration.fee import get_fee
from crypto.constants import TRANSACTION_TYPE_GROUP
from crypto.identity.private_key import PrivateKey
from crypto.identity.public_key import PublicKey
from crypto.transactions.serializer import Serializer
from crypto.transactions.signature import Signature
from crypto.transactions.transaction import Transaction

class BaseTransactionBuilder(object):
    transaction: Transaction

    def __init__(self):
        self.transaction = Transaction()

        if hasattr(self, 'transaction_type'):
            self.transaction.type = getattr(self, 'transaction_type')

        if hasattr(self, 'transaction_type'):
            self.transaction.fee = get_fee(getattr(self, 'transaction_type'))

        if hasattr(self, 'nonce'):
            self.transaction.nonce = getattr(self, 'nonce')

        if hasattr(self, 'signatures'):
            self.transaction.signatures = getattr(self, 'signatures')

        self.transaction.typeGroup = getattr(self, 'typeGroup', int(TRANSACTION_TYPE_GROUP.CORE))
        self.transaction.version = getattr(self, 'version', 1)
        self.transaction.expiration = getattr(self, 'expiration', 0)
        if self.transaction.type != 0:
            self.transaction.amount = getattr(self, 'amount', 0)

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

        msg = self.transaction.to_bytes(False, True, False)
        secret = unhexlify(PrivateKey.from_passphrase(passphrase).to_hex())
        self.transaction.signature = Signature.sign(msg, secret)
        self.transaction.id = self.transaction.get_id()

    def second_sign(self, passphrase):
        """Sign the transaction using the given second passphrase

        Args:
            passphrase (str): 2nd passphrase associated with the account sending this transaction
        """
        msg = self.transaction.to_bytes(False, True, False)
        secret = unhexlify(PrivateKey.from_passphrase(passphrase).to_hex())
        self.transaction.signSignature = Signature.sign(msg, secret)
        self.transaction.id = self.transaction.get_id()

    def multi_sign(self, passphrase, index):
        if not self.transaction.signatures:
            self.transaction.signatures = []

        if self.transaction.senderPublicKey is None:
            raise Exception('Sender Public Key is required for multi signature')

        index = len(self.transaction.signatures) if index == -1 else index

        msg = self.transaction.to_bytes()
        secret = unhexlify(PrivateKey.from_passphrase(passphrase).to_hex())
        signature = Signature.sign(msg, secret)

        index_formatted = hex(index).replace('x', '')
        self.transaction.signatures.append(index_formatted + signature)

    def serialize(self, skip_signature=False, skip_second_signature=False, skip_multi_signature=False):
        """Perform AIP11 compliant serialization.

        Args:
            skip_signature (bool, optional): do you want to skip the signature
            skip_second_signature (bool, optional): do you want to skip the 2nd signature
            skip_multi_signature (bool, optional): do you want to skip multi signature

        Returns:
            str: Serialized string
        """
        return Serializer(self.to_dict()).serialize(skip_signature, skip_second_signature, skip_multi_signature)

    def schnorr_verify(self):
        return self.transaction.verify_schnorr()

    def verify_secondsig_schnorr(self, secondPublicKey):
        return self.transaction.verify_secondsig_schnorr(secondPublicKey)

    def verify_multisig_schnorr(self):
        return self.transaction.verify_multisig_schnorr()

    def set_nonce(self, nonce):
        self.transaction.nonce = nonce

    def set_amount(self, amount: int):
        self.transaction.amount = amount

    def set_sender_public_key(self, public_key: str):
        self.transaction.senderPublicKey = public_key

    def set_expiration(self, expiration: int):
        self.transaction.expiration = expiration

    def set_type_group(self, type_group):
        if type(type_group) == int:
            self.transaction.typeGroup = type_group
        else:
            types = {TRANSACTION_TYPE_GROUP.TEST: 0, TRANSACTION_TYPE_GROUP.CORE: 1, TRANSACTION_TYPE_GROUP.RESERVED: 1000}
            self.transaction.typeGroup = types[type_group]
