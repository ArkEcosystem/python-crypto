import hashlib
from binascii import unhexlify

from crypto.identity.private_key import PrivateKey

from Cryptodome.Hash import keccak
from coincurve import PublicKey

class Address:
    @classmethod
    def from_public_key(cls, public_key: str) -> str:
        """Get an address from a public key

        Args:
            public_key (str): public key to get address

        Returns:
            str: address
        """

        public_key_bytes = PublicKey(bytes.fromhex(public_key)).format(compressed=False)[1:]

        keccak_hash = keccak.new(
            data=bytearray.fromhex(public_key_bytes.hex()),
            digest_bits=256,
        )

        return cls.get_checksum_address(unhexlify(keccak_hash.hexdigest()[22:]).hex())

    @classmethod
    def from_private_key(cls, private_key: str) -> str:
        """Get an address from private key

        Args:
            private_key (string): private key to get address

        Returns:
            str: address
        """
        private_key_object = PrivateKey.from_hex(private_key)

        return cls.from_public_key(private_key_object.public_key)

    @classmethod
    def from_passphrase(cls, passphrase: str) -> str:
        """Get an address from passphrase

        Args:
            passphrase (str): passphrase to get address

        Returns:
            str: address
        """
        private_key = hashlib.sha256(passphrase.encode()).hexdigest()

        return cls.from_private_key(private_key)

    @classmethod
    def get_checksum_address(cls, address: str) -> str:
        """Get checksum address

        Args:
            address (str): address to get checksum

        Returns:
            str: checksum address
        """
        address = address.lower()

        chars = list(address[2:])

        expanded = bytearray(40)
        for i in range(40):
            expanded[i] = ord(chars[i])

        hashed = keccak.new(data=bytes(expanded), digest_bits=256).digest()

        for i in range(0, 40, 2):
            if (hashed[i >> 1] >> 4) >= 8:
                chars[i] = chars[i].upper()
            if (hashed[i >> 1] & 0x0F) >= 8:
                chars[i + 1] = chars[i + 1].upper()

        return "0x" + ''.join(chars)
