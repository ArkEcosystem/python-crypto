import json
from binascii import unhexlify, hexlify

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
        message_bytes = message if isinstance(message, bytes) else message.encode()
        passphrase = passphrase.decode() if isinstance(passphrase, bytes) else passphrase
        private_key = PrivateKey.from_passphrase(passphrase)
        signature = private_key.sign(message_bytes)
        return cls(message, signature, private_key.public_key)

    def verify(self):
        """Verify the Message object

        Returns:
            bool: returns a boolean - true if verified, false if not
        """
        # print("INSIDE MESSAGE VERIFY")
        """
        {'public_key': '034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed192',
        'signature': b'24cb51a214057e4af4fd80cf3a96374c9c16ee1bcd7110684b5995eed1f19a49e08bf032feba18475cf888116826a03fc50c3cf52a7456e7e5085db1191b4568',
        'message': b'\xff\x02\x17\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03AQ\xa3\xecF\xb5g\nh+\nc9O\x865\x87\xd1\xbc\x97H;\x1blp\xebX\xe7\xf0\xae\xd1\x92\x80\x96\x98\x00\x00\x00\x00\x00\x00\x00\xc2\xeb\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x17\t\x95u\x02\x07\xec\xaf\x0c\xcf%\x1c\x12e\xb9*\xd8OU6b'}
        """
        # print("BEFORE MESSAGE")
        message = self.message if isinstance(self.message, bytes) else self.message.encode()
        # b'\xff\x02\x17\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03AQ\xa3\xecF\xb5g\nh+\nc9O\x865\x87\xd1\xbc\x97H;\x1blp\xebX\xe7\xf0\xae\xd1\x92\x80\x96\x98\x00\x00\x00\x00\x00\x00\x00\xc2\xeb\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x17\t\x95u\x02\x07\xec\xaf\x0c\xcf%\x1c\x12e\xb9*\xd8OU6b'
        key = PublicKey.from_hex(self.public_key)
        # {'public_key': <coincurve.keys.PublicKey object at 0x10e756d10>}
        signature = unhexlify(self.signature)
        #b'$\xcbQ\xa2\x14\x05~J\xf4\xfd\x80\xcf:\x967L\x9c\x16\xee\x1b\xcdq\x10hKY\x95\xee\xd1\xf1\x9aI\xe0\x8b\xf02\xfe\xba\x18G\\\xf8\x88\x11h&\xa0?\xc5\x0c<\xf5*tV\xe7\xe5\x08]\xb1\x19\x1bEh'
        is_verified = key.public_key.verify(signature, message)
        # print("Is verified")
        # Fuck up here
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
