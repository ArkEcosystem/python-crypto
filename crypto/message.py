from binascii import hexlify, unhexlify
from hashlib import sha256

from ecdsa import SECP256k1, SigningKey, VerifyingKey
from ecdsa.keys import BadDigestError, BadSignatureError
from ecdsa.util import sigdecode_der, sigencode_der_canonize

from crypto.exceptions import ArkBadDigestException, ArkBadSignatureException
from crypto.identity.keys import (
    privat_key_from_passphrase, public_key_from_passphrase, uncompress_ecdsa_public_key
)


def sign_message(message, passphrase):
    """Sign a message

    Args:
        message (bytes): a message you want to signature
        passphrase (bytes): passphrase you want to use to sign the message

    Returns:
        dict: dict containing message, public_key and a signature data
    """
    private_key = privat_key_from_passphrase(passphrase)
    signin_key = SigningKey.from_string(unhexlify(private_key), SECP256k1)
    signature = hexlify(
        signin_key.sign_deterministic(message, hashfunc=sha256, sigencode=sigencode_der_canonize)
    )
    data = {
        'message': message,
        'public_key': public_key_from_passphrase(passphrase),
        'signature': signature,
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
    uncompressed_public_key = uncompress_ecdsa_public_key(public_key)
    verifying_key = VerifyingKey.from_string(
        unhexlify(uncompressed_public_key),
        curve=SECP256k1,
        hashfunc=sha256
    )

    try:
        is_valid = verifying_key.verify(
            unhexlify(signature),
            message,
            hashfunc=sha256,
            sigdecode=sigdecode_der
        )
    except BadSignatureError:
        raise ArkBadSignatureException('Given signature was not valid')
    except BadDigestError as e:
        raise ArkBadDigestException(str(e))
    return is_valid
