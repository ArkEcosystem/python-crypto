from crypto.identity.private_key import PrivateKey
from btclib.ecc import ssa
from typing import Union

class Signature:
    @staticmethod
    def verify(signature, message, publicKey: Union[bytes, str]):
        # Remove leading byte ('02' / '03') from ECDSA key
        if (len(publicKey) == 33):
            publicKey = publicKey[1:]

        return ssa.verify(message, publicKey, signature)

    @staticmethod
    def sign(message, privateKey: Union[bytes, PrivateKey]):
        if isinstance(privateKey, PrivateKey):
            privateKey = bytes.fromhex(privateKey.to_hex())

        return ssa.sign(message, privateKey).serialize(False).hex()
