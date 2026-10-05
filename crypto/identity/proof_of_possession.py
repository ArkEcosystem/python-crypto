import sys
import os
from os.path import dirname

sys.path.append(os.path.join(dirname(dirname(__file__)), 'thirdparty/bls-signatures/python-impl'))

from schemes import PrivateKey as BLSSchemePrivateKey, core_sign_mpl

from crypto.configuration.network import Network
from crypto.exceptions import InvalidProofOfPossessionException
from crypto.identity.address import Address
from crypto.identity.bls_private_key import BLSPrivateKey

POP_DST = b'MAINSAIL_BLS_POP_BLS12381G2_XMD:SHA-256_SSWU_RO_POP_'


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

    @staticmethod
    def build_message(chain_id: int, registrant_address: str, public_key: bytes) -> bytes:
        """abi.encodePacked(uint256 chainId, address registrantAddress, bytes blsPublicKey)"""
        return chain_id.to_bytes(32, 'big') + bytes.fromhex(registrant_address[2:]) + public_key

    @staticmethod
    def validate_registrant_address(registrant_address: str) -> None:
        if not isinstance(registrant_address, str) or not Address.validate(registrant_address):
            raise InvalidProofOfPossessionException(
                f'Invalid registrant address: {registrant_address}'
            )

        hex_part = registrant_address[2:]
        is_single_case = hex_part == hex_part.lower() or hex_part == hex_part.upper()

        checksum_address = Address.get_checksum_address(registrant_address)

        if not is_single_case and checksum_address != registrant_address:
            raise InvalidProofOfPossessionException(
                f'Invalid registrant address checksum: {registrant_address}'
            )

    @classmethod
    def build_proof_of_possession(cls, private_key_bytes: bytes, registrant_address: str) -> dict:
        """Builds a proof of possession bound to the registrant address and the configured
        network chain ID.

        Args:
            private_key_bytes: 32-byte BLS private key
            registrant_address: address submitting the registration or update

        Returns:
            dict with 'pk' (hex, 48 bytes G1) and 'pop' (hex, 96 bytes G2)

        Raises:
            ValueError: if the key is not exactly 32 bytes or is the zero scalar
            InvalidProofOfPossessionException: if the registrant address is invalid
        """
        if int.from_bytes(private_key_bytes, 'big') == 0:
            raise ValueError('BLS secret key must not be zero')

        cls.validate_registrant_address(registrant_address)

        sk      = BLSSchemePrivateKey.from_bytes(private_key_bytes)
        pk      = bytes(sk.get_g1())
        message = cls.build_message(Network.get_network().chain_id(), registrant_address, pk)
        pop     = bytes(core_sign_mpl(sk, message, POP_DST))

        return {'pk': pk.hex(), 'pop': pop.hex()}

    @classmethod
    def from_passphrase(cls, passphrase: str, registrant_address: str) -> dict:
        """Convenience: derives private key from mnemonic and builds PoP.

        Returns:
            dict with 'pk' (hex, 48 bytes G1) and 'pop' (hex, 96 bytes G2)
        """
        return cls.build_proof_of_possession(
            cls.derive_bls_private_key(passphrase), registrant_address
        )
