import hashlib
from binascii import unhexlify

from crypto.identity.private_key import PrivateKey

from Cryptodome.Hash import keccak
from coincurve import PrivateKey, PublicKey

def get_checksum_address(address: str) -> str:
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

def address_from_public_key(public_key: str) -> str:
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

    return get_checksum_address(unhexlify(keccak_hash.hexdigest()[22:]).hex())

def address_from_private_key(private_key: str) -> str:
    """Get an address from private key

    Args:
        private_key (string): private key to get address

    Returns:
        str: address
    """
    private_key_object = PrivateKey.from_hex(private_key)

    return address_from_public_key(private_key_object.public_key.format(compressed=False).hex())

def address_from_passphrase(passphrase: str) -> str:
    """Get an address from passphrase

    Args:
        passphrase (str): passphrase to get address

    Returns:
        str: address
    """
    private_key = hashlib.sha256(passphrase.encode()).hexdigest()

    return address_from_private_key(private_key)
