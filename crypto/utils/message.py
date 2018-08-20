import json
from binascii import unhexlify

from crypto.identity.private_key import PrivateKey
from crypto.identity.public_key import PublicKey


class Message(object):

    def __init__(self, message, signature, public_key):
        self.public_key = public_key
        self.signature = signature
        self.message = message

    @classmethod
    def sign(cls, message, passphrase):
        """Signs a message

        Args:
            message (str/bytes): a message you wish to sign
            passphrase (str/byes): passphrase you wish to use to sign the message

        Returns:
            Message: returns a message object
        """
        message_byes = message if isinstance(message, bytes) else message.encode()
        passphrase = passphrase.decode() if isinstance(passphrase, bytes) else passphrase
        private_key = PrivateKey.from_passphrase(passphrase)
        signature = private_key.sign(message_byes)
        return cls(message, signature, private_key.public_key)

    def verify(self):
        """Verify the Message object

        Returns:
            bool: returns a boolean - true if verified, false if not
        """
        message = self.message if isinstance(self.message, bytes) else self.message.encode()
        key = PublicKey.from_hex(self.public_key)
        signature = unhexlify(self.signature)
        is_verified = key.public_key.verify(signature, message)
        return is_verified

    def to_dict(self):
        """Return a dictionary of the message

        Returns:
            dict: dictionary consiting of public_key, signature and message
        """
        data = {
            'public_key': self.public_key,
            'signature': self.signature,
            'message': self.message,
        }
        return data

    def to_json(self):
        """Returns a json string of the the message

        Returns:
            str: json string consisting of public_key, signature and message
        """
        data = self.to_dict()
        return json.dumps(data)
