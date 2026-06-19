import hashlib

from base58 import b58decode_check, b58encode_check

from Cryptodome.Hash import RIPEMD160

from crypto.identity.private_key import PrivateKey


class LegacyAddress:
    @classmethod
    def from_public_key(cls, public_key: str, pub_key_hash: int) -> str:
        ripemd160 = RIPEMD160.new(bytes.fromhex(public_key))
        payload = bytes([pub_key_hash]) + ripemd160.digest()
        return b58encode_check(payload).decode()

    @classmethod
    def from_private_key(cls, private_key: str, pub_key_hash: int) -> str:
        public_key = PrivateKey.from_hex(private_key).public_key
        return cls.from_public_key(public_key, pub_key_hash)

    @classmethod
    def from_passphrase(cls, passphrase: str, pub_key_hash: int) -> str:
        private_key = hashlib.sha256(passphrase.encode()).hexdigest()
        return cls.from_private_key(private_key, pub_key_hash)

    @classmethod
    def validate(cls, address: str, pub_key_hash: int) -> bool:
        try:
            decoded = b58decode_check(address)
            if len(decoded) != 21:
                return False
            return decoded[0] == pub_key_hash
        except Exception:
            return False
