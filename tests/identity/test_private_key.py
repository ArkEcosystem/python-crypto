from crypto.identity.private_key import PrivateKey



from binascii import hexlify, unhexlify
from hashlib import sha256

from coincurve import PrivateKey as PvtKey
from btclib.to_prv_key import PrvKey, int_from_prv_key, prv_keyinfo_from_prv_key, _prv_keyinfo_from_xprv
from btclib.to_pub_key import pub_keyinfo_from_key
from btclib.ecc import bms
from btclib.b58 import p2pkh
from btclib.ecc import dsa
# from btclib.bip32 import BIP32KeyData
from coincurve.ecdsa import der_to_cdata, serialize_compact, deserialize_compact

from btclib.network import (
    NETWORKS,
)



def test_private_key_from_passphrase(identity):
    private_key = PrivateKey.from_passphrase(identity['passphrase'])
    assert isinstance(private_key, PrivateKey)
    assert private_key.to_hex() == identity['data']['private_key']


def test_private_key_from_hex(identity):
    private_key = PrivateKey.from_hex(identity['data']['private_key'])
    assert isinstance(private_key, PrivateKey)
    assert private_key.to_hex() == identity['data']['private_key']

def test_sign_compact(sign_compact):
    private_key = PrivateKey.from_passphrase(sign_compact['passphrase'])

    message = bytes.fromhex(sign_compact['data']['message'])
    signature = private_key.sign_compact(message)

    if isinstance(signature, str) or isinstance(signature, bytes):
        serialized = signature
    else:
        serialized = signature.serialize()

    # assert serialized[0] == 27
    assert serialized.hex() == sign_compact['data']['serialized']
