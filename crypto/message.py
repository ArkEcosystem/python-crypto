from binascii import hexlify, unhexlify
from hashlib import sha256

from bit.format import verify_sig

from coincurve import PrivateKey


def sign_message(message, passphrase):
    """Sign a message

    Args:
        message (bytes): a message you want to signature
        passphrase (str): passphrase you want to use to sign the message

    Returns:
        dict: dict containing message, public_key and a signature data
    """
    private_key = PrivateKey.from_hex(sha256(passphrase.encode()).hexdigest())
    signature = private_key.sign(message)
    data = {
        'message': message,
        'public_key': hexlify(private_key.public_key.format()).decode(),
        'signature': hexlify(signature).decode(),
    }
    return data


def verify_message(message, public_key, signature):
    """Verify a message

    Args:
        message (str): a message you want to verify
        public_key (str): public key used to verify a message
        signature (str): signature of a signed message

    Returns:
        bool: boolean indicating if a message is valid or not
    """
    is_valid = verify_sig(
        signature=unhexlify(signature.encode()),
        data=message.encode(),
        public_key=unhexlify(public_key.encode())
    )
    return is_valid
