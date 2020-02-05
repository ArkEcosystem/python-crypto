import hashlib
from binascii import hexlify, unhexlify

from crypto.configuration.fee import get_fee
from crypto.constants import HTLC_LOCK_EXPIRATION_TYPE, TRANSACTION_TYPE_GROUP
from crypto.identity.private_key import PrivateKey
from crypto.identity.public_key import PublicKey
from crypto.schnorr import schnorr
from crypto.transactions.transaction import Transaction
from crypto.utils.message import Message


class BaseTransactionBuilder(object):

    def __init__(self):
        self.transaction = Transaction()
        self.transaction.type = getattr(self, 'transaction_type', None)
        self.transaction.fee = get_fee(getattr(self, 'transaction_type', None))
        self.transaction.nonce = getattr(self, 'nonce', None)
        self.transaction.typeGroup = getattr(self, 'typeGroup', 1)
        self.transaction.signatures = getattr(self, 'signatures', None)
        self.transaction.version = getattr(self, 'version', 2)
        if self.transaction.type != 0:
            self.transaction.amount = getattr(self, 'amount', 0)

    def to_dict(self):
        return self.transaction.to_dict()

    def to_json(self):
        return self.transaction.to_json()

    def schnorr_sign(self, passphrase):
        """Sign the transaction using the given passphrase

        Args:
            passphrase (str): passphrase associated with the account sending this transaction
        """
        self.transaction.senderPublicKey = PublicKey.from_passphrase(passphrase)
        msg = hashlib.sha256(self.transaction.to_bytes(False, True, False)).digest()
        secret = unhexlify(PrivateKey.from_passphrase(passphrase).to_hex())
        self.transaction.signature = hexlify(schnorr.bcrypto410_sign(msg, secret))
        self.transaction.id = self.transaction.get_id()

    def second_sign(self, passphrase):
        """Sign the transaction using the given second passphrase

        Args:
            passphrase (str): 2nd passphrase associated with the account sending this transaction
        """
        msg = hashlib.sha256(self.transaction.to_bytes(False, True, False)).digest()
        secret = unhexlify(PrivateKey.from_passphrase(passphrase).to_hex())
        self.transaction.signSignature = hexlify(schnorr.bcrypto410_sign(msg, secret))   
        self.transaction.id = self.transaction.get_id()

    def multi_sign(self, passphrase, index):
        if not self.transaction.signatures:
            self.transaction.signatures = []

        index = len(self.transaction.signatures) if index == -1 else index

        msg = hashlib.sha256(self.transaction.to_bytes()).digest()
        secret = unhexlify(PrivateKey.from_passphrase(passphrase).to_hex())
        signature = hexlify(schnorr.bcrypto410_sign(msg, secret))

        index_formatted = hex(index).replace('x', '')
        self.transaction.signatures.append(index_formatted + signature.decode())

    def schnorr_verify(self):
        return self.transaction.verify_schnorr()
    
    def schnorr_verify_second(self, secondPublicKey):
        return self.transaction.verify_schnorr_secondsig(secondPublicKey)

    def schnorr_verify_multisig(self):
        return self.transaction.verify_schnorr_multisig()

    def set_nonce(self, nonce):
        self.transaction.nonce = nonce

    def set_amount(self, amount):
        self.transaction.amount = amount

    def set_sender_public_key(self, public_key):
        self.transaction.senderPublicKey = public_key

    def set_expiration(self, expiration):
        if type(expiration) == int:
            self.transaction.expiration = expiration
        else:
            types = {HTLC_LOCK_EXPIRATION_TYPE.EPOCH_TIMESTAMP: 1, HTLC_LOCK_EXPIRATION_TYPE.BLOCK_HEIGHT: 2}
            self.transaction.expiration = types[expiration]

    def set_type_group(self, type_group):
        if type(type_group) == int:
            self.transaction.typeGroup = type_group
        else:
            types = {TRANSACTION_TYPE_GROUP.TEST: 0, TRANSACTION_TYPE_GROUP.CORE: 1, TRANSACTION_TYPE_GROUP.RESERVED: 1000}
            self.transaction.typeGroup = types[type_group]
