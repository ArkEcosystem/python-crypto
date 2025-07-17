import json
from binascii import unhexlify
from typing import Union

from Cryptodome.Hash import keccak

from crypto.identity.private_key import PrivateKey
from crypto.identity.public_key import PublicKey

MESSAGE_PREFIX = b"\x19Ethereum Signed Message:\n"

class Message(object):
    public_key: bytes
    message: bytes
    signature: bytes

    def __init__(self, public_key: Union[bytes, str], message: Union[bytes, str], signature: Union[bytes, str]):
        if isinstance(public_key, str):
            self.public_key = public_key.encode()
        else:
            self.public_key = public_key

        if isinstance(message, str):
            self.message = message.encode()
        else:
            self.message = message

        if isinstance(signature, str):
            self.signature = signature.encode()
        else:
            self.signature = signature

    @staticmethod
    def new(public_key: Union[bytes, str], message: Union[bytes, str], signature: Union[bytes, str]):
        """Creates a new message object

        Returns:
            Message: returns a message object
        """
        return Message(
            public_key=public_key,
            message=message,
            signature=signature,
        )

    @classmethod
    def sign(cls, message: Union[bytes, str], passphrase: Union[bytes, str]):
        """Signs a message

        Args:
            message (str/bytes): a message you wish to sign
            passphrase (str/byes): passphrase you wish to use to sign the message

        Returns:
            Message: returns a message object
        """

        if isinstance(message, str):
            message = message.encode()

        if not isinstance(passphrase, str):
            passphrase = passphrase.hex()

        private_key = PrivateKey.from_passphrase(passphrase)
        public_key = private_key.public_key

        transaction_signature = private_key.sign(MESSAGE_PREFIX + (str(len(message))).encode() + message)

        signature_v = bytes([transaction_signature[0]]).hex()
        signature_r = transaction_signature[1:33].hex()
        signature_s = transaction_signature[33:].hex()

        signature = signature_r + signature_s + signature_v

        return cls(
            message=message,
            signature=signature,
            public_key=public_key,
        )

    def verify(self):
        """Verify the Message object

        Returns:
            bool: returns a boolean - true if verified, false if not
        """

        signature = unhexlify(self.signature)

        message = MESSAGE_PREFIX + (str(len(self.message))).encode() + self.message
        message_hash = keccak.new(data=message, digest_bits=256).digest()

        signature_r = signature[0:32]
        signature_s = signature[32:64]
        signature_v = signature[64]

        signature = signature_r + signature_s + bytes([signature_v])

        public_key = PublicKey.recover(message_hash, signature)

        return public_key.public_key == unhexlify(self.public_key).hex()

    def to_dict(self):
        """Return a dictionary of the message

        Returns:
            dict: dictionary consiting of public_key, signature and message
        """
        data = {
            'public_key': self.public_key.decode(),
            'signature': self.signature.decode(),
            'message': self.message.decode(),
        }
        return data

    def to_json(self):
        """Returns a json string of the the message

        Returns:
            str: json string consisting of public_key, signature and message
        """
        data = self.to_dict()

        return json.dumps(data)

    def __str__(self):
        """Returns a string representation of the message

        Returns:
            str: string representation of the message
        """
        return self.to_json()
