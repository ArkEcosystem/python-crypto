from crypto.configuration.fee import get_fee
from crypto.identity.public_key import PublicKey
from crypto.identity.private_key import PrivateKey
from crypto.transactions.transaction import Transaction
from crypto.utils.message import Message
from crypto.constants import TRANSACTION_TYPE_GROUP

import hashlib
from binascii import unhexlify, hexlify
from crypto.schnorr import schnorr


class BaseTransactionBuilder(object):

    def __init__(self):
        self.transaction = Transaction()
        self.transaction.type = getattr(self, 'transaction_type', None)
        self.transaction.fee = get_fee(getattr(self, 'transaction_type', None))
        self.transaction.nonce = getattr(self, 'nonce', None)
        self.transaction.typeGroup = getattr(self, 'typeGroup', 1)
        self.transaction.signatures = getattr(self, 'signatures', [])


    def to_dict(self):
        return self.transaction.to_dict()


    def to_json(self):
        return self.transaction.to_json()

    def schnorr_sign(self, passphrase):
        #print(self.transaction)
        #transaction = Transaction(*)
        #msg = hashlib.sha256(unhexlify(transaction.serialize())).digest()
        #print(passphrase)
        #print(self.transaction.senderPublicKey)
        self.transaction.senderPublicKey = PublicKey.from_passphrase(passphrase)
        #print(self.transaction.senderPublicKey)
        msg = hashlib.sha256(self.transaction.to_bytes(False, True, False)).digest()
        secret = unhexlify(PrivateKey.from_passphrase(passphrase).to_hex())
        #print("YOYO")
        #print(hashlib.sha256(unhexlify(self.transaction.to_bytes(False, True, False))).hexdigest())
        self.transaction.signature = hexlify(schnorr.bcrypto410_sign(msg, secret))
        self.transaction.id = self.transaction.get_id()


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

    def multi_sign(self, passphrase, index):
        if not self.transaction.signatures:
            self.transaction.signatures = []
        self.set_version(2)

        index = len(self.transaction.signatures) if index == -1 else index

        msg = hashlib.sha256(self.transaction.to_bytes()).digest()
        secret = unhexlify(PrivateKey.from_passphrase(passphrase).to_hex())
        signature = hexlify(schnorr.bcrypto410_sign(msg, secret))

        index_formatted = hex(index).replace('x', '')
        self.transaction.signatures.append(index_formatted + signature.decode())


    def verify(self):
        self.transaction.verify()

    def schnorr_verify(self):
        self.transaction.schnorr_verify()

    def schnorr_verify_bis(self):
        self.transaction.test_verify_bis()

    def second_verify(self):
        self.transaction.second_verify()


    def set_version(self, version=2):
        self.transaction.version = version


    def set_nonce(self, nonce):
        self.transaction.nonce = nonce


    def set_amount(self, amount):
        self.transaction.amount = amount


    def set_network(self, network):
        self.transaction.network = network

    def set_sender_public_key(self, public_key):
        self.transaction.senderPublicKey = public_key


    def set_expiration(self, expiration):
        if type(expiration) == int:
            self.transaction.expiration = expiration
        else:
            types = {EPOCH_TIMESTAMP: 1, BLOCK_HEIGHT: 2}
            self.transaction.expiration = types[expiration]


    def set_type_group(self, type_group):
        if type(type_group) == int:
            self.transaction.typeGroup = type_group
        else:
            types = {TRANSACTION_TYPE_GROUP.TEST: 0, TRANSACTION_TYPE_GROUP.CORE: 1, TRANSACTION_TYPE_GROUP.RESERVED: 1000}
            self.transaction.typeGroup = types[type_group]
