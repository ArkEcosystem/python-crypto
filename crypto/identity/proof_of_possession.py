import sys
import os
from os.path import dirname

sys.path.append(os.path.join(dirname(dirname(__file__)), 'thirdparty/bls-signatures/python-impl'))

from schemes import PopSchemeMPL, PrivateKey as BLSSchemePrivateKey

from crypto.identity.bls_private_key import BLSPrivateKey


class ProofOfPossession:
    @staticmethod
    def derive_bls_private_key(passphrase: str) -> bytes:
        """Derives a BLS private key (32 bytes) from a BIP-39 mnemonic."""
        return BLSPrivateKey.from_passphrase(passphrase).private_key

    @classmethod
    def derive_bls_public_key(cls, passphrase: str) -> str:
        """Derives the BLS12-381 G1 public key from a mnemonic. Returns hex (96 chars)."""
        sk = BLSSchemePrivateKey.from_bytes(cls.derive_bls_private_key(passphrase))
        return bytes(sk.get_g1()).hex()

    @classmethod
    def build_proof_of_possession(cls, private_key_bytes: bytes) -> dict:
        """Builds proof of possession for a given private key.

        Args:
            private_key_bytes: 32-byte BLS private key

        Returns:
            dict with 'pk' (hex, 48 bytes G1) and 'pop' (hex, 96 bytes G2)

        Raises:
            ValueError: if the key is not exactly 32 bytes or is the zero scalar
        """
        if int.from_bytes(private_key_bytes, 'big') == 0:
            raise ValueError('BLS secret key must not be zero')

        sk  = BLSSchemePrivateKey.from_bytes(private_key_bytes)
        pk  = bytes(sk.get_g1()).hex()
        pop = bytes(PopSchemeMPL.pop_prove(sk)).hex()

        return {'pk': pk, 'pop': pop}

    @classmethod
    def from_passphrase(cls, passphrase: str) -> dict:
        """Convenience: derives private key from mnemonic and builds PoP.

        Returns:
            dict with 'pk' (hex, 48 bytes G1) and 'pop' (hex, 96 bytes G2)
        """
        return cls.build_proof_of_possession(cls.derive_bls_private_key(passphrase))
