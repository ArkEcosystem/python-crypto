from binascii import hexlify, unhexlify
from hashlib import sha256
import traceback
import btclib.mnemonic

import btclib.mnemonic.bip39
from coincurve import PublicKey as PubKey
import py_ecc

import blspy
from blspy import PrivateKey, AugSchemeMPL, G1Element, BasicSchemeMPL, PopSchemeMPL
import py_ecc.bls.g2_primitives
import py_ecc.bls.hash
import py_ecc.bls.hash_to_curve
import py_ecc.bls.point_compression
import py_ecc.bls12_381
import py_ecc.bls12_381
from py_ecc import bn128

import hkdf

from py_ecc.bls import G2ProofOfPossession as bls_pop

import crypto.utils.bls as my_bls

def generate_public_key(private_key):
    """
    Derive the BLS public key from a given private key.

    Args:
    - private_key (int): The BLS private key.

    Returns:
    - tuple: The BLS public key (x, y) coordinates on the curve.
    """
    public_key = bls_pop.SkToPk(private_key)
    return public_key


def eip_2333_keygen(entropy):
    """
    Generate a BLS private key according to EIP-2333.

    Args:
    - entropy (bytes): The entropy source for key generation.

    Returns:
    - int: The generated BLS private key.
    """
    salt = b"BLS-SIG-KEYGEN-SALT-"
    SK = 0

    while SK == 0:
        # Hash the salt
        salt = sha256(salt).digest()

        # HKDF-Extract
        prk = hkdf.hkdf_extract(salt, entropy + b'\x00')

        # HKDF-Expand
        okm = hkdf.hkdf_expand(prk, b"", bn128.bn128_curve.curve_order.bit_length() // 8)

        # Convert OKM to integer and reduce modulo r
        SK = int.from_bytes(okm, byteorder='big') % bn128.bn128_curve.curve_order

    return SK























class BLSPublicKey:

    def __init__(self, public_key: str):
        self.public_key = PubKey(unhexlify(public_key.encode()))

    def to_hex(self) -> str:
        return hexlify(self.public_key.format()).decode()

    # def hkdfModR(self, ikm, key_info):
    #     pass

    # def derive_master(seed):
    #     pass

    # def derive_child(parentKey, index):
    #     pass

    @classmethod
    def from_passphrase(cls, passphrase: str) -> str:
        # # Hash the passphrase to create a consistent seed
        # seed = sha256(passphrase.encode()).digest()
        # seed = unhexlify(sha256(passphrase.encode()).hexdigest())
        # seed = hexlify(passphrase.encode())

        # # Generate a private key from the seed
        # py_ecc.bls12_381.bls12_381_pairing.
        seed = btclib.mnemonic.bip39.seed_from_mnemonic(passphrase, '')
        # print('seed', hexlify(seed))
        # seed = btclib.mnemonic.bip39.entropy_from_mnemonic(passphrase).encode()

        private_key = my_bls.deriveChild(my_bls.deriveMaster(seed), 0).hex()
        public_key = generate_public_key(private_key).hex()

        return

























        # private_key = BasicSchemeMPL.key_gen(seed)
        # seed = unhexlify(bytes(private_key).hex())
        # child_pk: PrivateKey = AugSchemeMPL.derive_child_sk(private_key, 152)
        # seed = unhexlify(bytes(child_pk).hex())





        private_key = eip_2333_keygen(seed)
        public_key = generate_public_key(private_key).hex()


        # private_key = py_ecc.optimized_bls12_381.optimized_swu.sqrt_division_FQ2(int.from_bytes(seed, byteorder='big'))
        # public_key = py_ecc.bls12_381.bls12_381_curve.multiply(bn128.bn128_curve.G1, private_key)

        # return public_key

        return public_key




















        seed = btclib.mnemonic.bip39.seed_from_mnemonic(passphrase, '')
        print(seed.hex().encode())
        print()

        private_key = unhexlify(sha256(passphrase.encode()).hexdigest()) #hexlify(passphrase.encode()) #sha256(passphrase.encode()).hexdigest()
        # private_key = hexlify(passphrase.encode()) #sha256(passphrase.encode()).hexdigest()
        # private_key = sha256(passphrase.encode()).hexdigest()
        # private_key = unhexlify(seed.hex().encode())
        # private_key = hexlify(private_key)
        print(len(private_key), private_key)
        attempts = {
            'AugSchemeMPL': AugSchemeMPL.key_gen(seed.hex().encode()),
            'BasicSchemeMPL': BasicSchemeMPL.key_gen(seed.hex().encode()),
            'PopSchemeMPL': PopSchemeMPL.key_gen(seed.hex().encode()),
            'PrivateKey.from_bytes': blspy.PrivateKey.from_bytes(private_key)
        }

        for attempt_name in attempts:
            attempt = attempts[attempt_name]
            print(attempt_name)
            master_sk = attempt
            child: PrivateKey = AugSchemeMPL.derive_child_sk(master_sk, 152)
            grandchild: PrivateKey = AugSchemeMPL.derive_child_sk(child, 952)

            master_pk: G1Element = master_sk.get_g1()
            child_u: PrivateKey = AugSchemeMPL.derive_child_sk_unhardened(master_sk, 22)
            grandchild_u: PrivateKey = AugSchemeMPL.derive_child_sk_unhardened(child_u, 0)

            child_u_pk: G1Element = AugSchemeMPL.derive_child_pk_unhardened(master_pk, 22)
            grandchild_u_pk: G1Element = AugSchemeMPL.derive_child_pk_unhardened(child_u_pk, 0)

            print('master_sk', master_sk)
            print('child', child)
            print('grandchild', grandchild)
            print('master_pk', master_pk)
            print('child_u', child_u)
            print('grandchild_u', grandchild_u)
            print('child_u_pk', child_u_pk)
            print('grandchild_u_pk', grandchild_u_pk)
            print()

            print('master_sk g1', bytes(master_sk.get_g1()).hex())
            print('child g1', bytes(child.get_g1()).hex())
            print('grandchild g1', bytes(grandchild.get_g1()).hex())
            # print('master_pk g1', master_pk.get_g1())
            print('child_u g1', bytes(child_u.get_g1()).hex())
            print('grandchild_u g1', bytes(grandchild_u.get_g1()).hex(), len(bytes(grandchild_u.get_g1()).hex()))
            # print('child_u_pk g1', child_u_pk.get_g1())
            # print('grandchild_u_pk g1', grandchild_u_pk.get_g1())

            print()
            print()
            print()


        return master_sk.get_g1()
        # return child.get_g1()
        # # return grandchild.get_g1()
        # return grandchild_u.get_g1()


        # sk = blspy.BasicSchemeMPL.key_gen(seed)

        # # print(sk, pk)

        # # pk = blspy.PrivateKey.from_seed(seed)
        # # sk: blspy.PrivateKey = blspy.AugSchemeMPL.key_gen(seed)
        # private_key = unhexlify(sha256(passphrase.encode()).hexdigest())
        # sk = blspy.PrivateKey.from_bytes(private_key)

        # pk = sk.get_g1()

        return pk












        # print(hexlify(passphrase.encode()))
        # # print(sha256(passphrase.encode()).hexdigest())

        # private_key =


        # L = 48
        # # `ceil((3 * ceil(log2(r))) / 16)`, where `r` is the order of the BLS 12-381 curve
        # okm = extract_expand(L, seed + bytes([0]), b"BLS-SIG-KEYGEN-SALT-", bytes([0, L]))
        # return PrivateKey(int.from_bytes(okm, "big") % default_ec.n)





        # seed = btclib.mnemonic.bip39.seed_from_mnemonic(passphrase, '')

        # private_key = unhexlify(sha256(passphrase.encode()).hexdigest()) #hexlify(passphrase.encode()) #sha256(passphrase.encode()).hexdigest()
        # # private_key = unhexlify(sha256(passphrase.encode()).hexdigest()) #hexlify(passphrase.encode()) #sha256(passphrase.encode()).hexdigest()
        # # private_key = sha256(passphrase.encode()).hexdigest()

        # print('private_key', private_key)

        # private_key = seed

        # try:
        #     print('seed', seed)

        #     return blspy.PrivateKey.from_bytes(private_key)
        # except Exception as e:
        #     print(e, traceback.print_exc())

        # return blspy.PrivateKey.from_bytes(private_key) #.get_public_key().serialize()
        # return blspy.PrivateKey.from_bytes(private_key.encode()) #.get_public_key().serialize()

        # return private_key.public_key

    @classmethod
    def from_hex(cls, public_key):
        return cls(public_key)
