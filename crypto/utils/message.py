import json
from binascii import unhexlify

from crypto.identity.private_key import PrivateKey
from crypto.transactions.signature import Signature
from typing import Union

class Message(object):
    public_key: bytes
    message: bytes
    signature: bytes

    def __init__(self, public_key: bytes, message: bytes, signature: bytes):
        if type(public_key) is bytes:
            self.public_key = public_key
        else:
            self.public_key = public_key.encode()

        if type(message) is bytes:
            self.message = message
        else:
            self.message = message.encode()

        if type(signature) is bytes:
            self.signature = signature
        else:
            self.signature = signature.encode()

    @classmethod
    def sign(cls, message: Union[bytes, str], passphrase: bytes):
        """Signs a message

        Args:
            message (str/bytes): a message you wish to sign
            passphrase (str/byes): passphrase you wish to use to sign the message

        Returns:
            Message: returns a message object
        """

        if type(message) is str:
            message = message.encode()


        private_key = PrivateKey.from_passphrase(passphrase)
        public_key = private_key.public_key
        signature = Signature.sign(message, private_key)

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

        public_key = unhexlify(self.public_key)
        signature = unhexlify(self.signature)

        return Signature.verify(signature, self.message, public_key)

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
