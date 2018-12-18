import json
from binascii import unhexlify

from crypto.identity.private_key import PrivateKey
from crypto.identity.public_key import PublicKey


class Message(object):
    def __init__(self, **kwargs):
        for k in kwargs.keys():
            if k in ['message', 'signature', 'publickey', 'publicKey']:
                self.__setattr__(k, kwargs[k])
            else:
                raise TypeError('Invalid keyword argument %s' % k)

    @classmethod
    def sign(cls, message, passphrase):
        """Signs a message

        Args:
            message (str/bytes): a message you wish to sign
            passphrase (str/byes): passphrase you wish to use to sign the message

        Returns:
            Message: returns a message object
        """
        message_bytes = message if isinstance(message, bytes) else message.encode()
        passphrase = passphrase.decode() if isinstance(passphrase, bytes) else passphrase
        private_key = PrivateKey.from_passphrase(passphrase)
        signature = private_key.sign(message_bytes)
        return cls(message=message, signature=signature, publicKey=private_key.public_key)

    def verify(self):
        """Verify the Message object

        Returns:
            bool: returns a boolean - true if verified, false if not
        """
        message = self.message if isinstance(self.message, bytes) else self.message.encode()
        key = PublicKey.from_hex(self.publickey) if hasattr(self, 'publickey') else PublicKey.from_hex(self.publicKey)
        signature = unhexlify(self.signature)
        is_verified = key.public_key.verify(signature, message)
        return is_verified

    def to_dict(self):
        """Return a dictionary of the message

        Returns:
            dict: dictionary consiting of public_key, signature and message
        """
        data = {
            ('publicKey' if hasattr(self, 'publicKey') else 'publickey'): (self.publicKey if hasattr(self, 'publicKey') else self.publickey),
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
