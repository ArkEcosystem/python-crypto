from binascii import hexlify, unhexlify
from hashlib import sha256
import traceback
import btclib.mnemonic

import btclib.mnemonic.bip39
from coincurve import PublicKey as PubKey
import py_ecc

import blspy
from blspy import PrivateKey, AugSchemeMPL, G1Element, BasicSchemeMPL, PopSchemeMPL
from py_ecc import bn128

import crypto.utils.bls as my_bls

class BLSPublicKey:

    def __init__(self, public_key: str):
        self.public_key = PubKey(unhexlify(public_key.encode()))

    def to_hex(self) -> str:
        return hexlify(self.public_key.format()).decode()

    @classmethod
    def from_passphrase_attempt_1(cls, passphrase: str) -> str:
        # seed = sha256(passphrase.encode()).digest()
        # seed = unhexlify(sha256(passphrase.encode()).hexdigest())
        # seed = hexlify(passphrase.encode())
        seed = btclib.mnemonic.bip39.seed_from_mnemonic(passphrase, '')
        seed = bytes('1234'.encode())

        private_key = my_bls.deriveChild(my_bls.deriveMaster(seed), 0).hex()
        # public_key = generate_public_key(private_key).hex()
        public_key = private_key

        return public_key


    @classmethod
    def from_passphrase_attempt_2(cls, passphrase: str) -> str:
        seed = btclib.mnemonic.bip39.seed_from_mnemonic(passphrase, '')
        seed = btclib.mnemonic.bip39.entropy_from_mnemonic(passphrase).encode()

        private_key = my_bls.eip_2333_keygen(seed)
        # public_key = my_bls.generate_public_key(private_key).hex()

        public_key = py_ecc.bls12_381.bls12_381_curve.multiply(bn128.bn128_curve.G1, private_key)

        return public_key


    @classmethod
    def from_passphrase_attempt_3(cls, passphrase: str) -> str:
        seed = btclib.mnemonic.bip39.seed_from_mnemonic(passphrase, '')
        # print(seed.hex().encode())
        # print()

        private_key = unhexlify(sha256(passphrase.encode()).hexdigest()) #hexlify(passphrase.encode()) #sha256(passphrase.encode()).hexdigest()
        # private_key = hexlify(passphrase.encode()) #sha256(passphrase.encode()).hexdigest()
        # private_key = sha256(passphrase.encode()).hexdigest()
        # private_key = unhexlify(seed.hex().encode())
        # private_key = hexlify(private_key)

        # print(len(private_key), private_key)
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


    @classmethod
    def from_passphrase_attempt_4(cls, passphrase: str) -> str:
        seed = btclib.mnemonic.bip39.seed_from_mnemonic(passphrase, '')
        sk = blspy.BasicSchemeMPL.key_gen(seed)

        # pk = blspy.PrivateKey.from_seed(seed)
        pk = unhexlify(sha256(passphrase.encode()).hexdigest())
        sk = blspy.PrivateKey.from_bytes(pk)

        return sk.get_g1()


    @classmethod
    def from_passphrase_attempt_5(cls, passphrase: str) -> str:
        # seed = btclib.mnemonic.bip39.seed_from_mnemonic(passphrase, '')

        # private_key = unhexlify(sha256(passphrase.encode()).hexdigest()) #hexlify(passphrase.encode()) #sha256(passphrase.encode()).hexdigest()
        private_key = unhexlify(sha256(passphrase.encode()).hexdigest()) #hexlify(passphrase.encode()) #sha256(passphrase.encode()).hexdigest()
        # private_key = sha256(passphrase.encode()).hexdigest()

        # print('private_key', private_key)

        # private_key = seed

        try:
            # print('seed', seed)

            return blspy.PrivateKey.from_bytes(private_key)
        except Exception as e:
            print(e, traceback.print_exc())

        return blspy.PrivateKey.from_bytes(private_key) #.get_public_key().serialize()
        return blspy.PrivateKey.from_bytes(private_key.encode()) #.get_public_key().serialize()

        return private_key.public_key

    @classmethod
    def from_hex(cls, public_key):
        return cls(public_key)
