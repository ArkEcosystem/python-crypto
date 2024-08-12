import hashlib
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.exceptions import InvalidSignature

def i2osp(index, length):
    """ Convert integer to octet string """
    return index.to_bytes(length, byteorder='big')

def os2ip(data):
    """ Convert octet string to integer """
    return int.from_bytes(data, byteorder='big')

def concatBytes(*args):
    """ Concatenate bytes objects """
    return b''.join(args)

def utf8ToBytes(s):
    """ Convert UTF-8 string to bytes """
    return s.encode('utf-8')

def sha256(data):
    """ Compute SHA-256 hash of data """
    return hashlib.sha256(data).digest()

def hkdf(hash_algo, ikm, salt, info=b'', length=None):
    """ HKDF key derivation function """
    if length is None:
        length = hash_algo.digest_size
    hkdf_obj = HKDF(algorithm=hash_algo(), salt=salt, info=info, length=length)
    return hkdf_obj.derive(ikm)

def blsR():
    """ Placeholder for curve order r, replace with actual value """
    # This should be replaced with the actual curve order for BLS
    return 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEC2F63BDC9064449C8943E350C0A7DC19D7

def assertUint32(value):
    """ Assert value fits within uint32 range """
    if not 0 <= value < 2**32:
        raise ValueError("Value out of uint32 range")

def ikmToLamportSK(ikm, salt):
    """ Generate Lamport secret key from IKM and salt """
    hashed = sha256(concatBytes(ikm, salt))
    return hashed

def parentSKToLamportPK(parentSK, index):
    """ Convert parent secret key to Lamport public key """
    if not isinstance(parentSK, bytes):
        raise TypeError('Expected bytes')
    assertUint32(index)
    salt = i2osp(index, 4)
    ikm = parentSK
    lamport0 = ikmToLamportSK(ikm, salt)
    notIkm = bytes(~byte & 0xFF for byte in parentSK)
    lamport1 = ikmToLamportSK(notIkm, salt)
    lamportPK = [sha256(part) for part in [lamport0, lamport1]]
    return sha256(concatBytes(*lamportPK))

def hkdfModR(ikm, keyInfo=b''):
    """ HKDF-based key derivation function """
    salt = utf8ToBytes('BLS-SIG-KEYGEN-SALT-')
    SK = 0
    input = concatBytes(ikm, b'\x00')
    label = concatBytes(keyInfo, b'\x00\x30')
    while SK == 0:
        salt = sha256(salt)
        okm = hkdf(hashes.SHA256, input, salt, info=label, length=48)
        SK = os2ip(okm) % blsR()
    return (SK % (2**256)).to_bytes(32, byteorder='big')  # Adjusted to fit within 32 bytes
    return SK.to_bytes(32, byteorder='big')

def deriveMaster(seed):
    """ Derive master secret key """
    return hkdfModR(seed)

def deriveChild(parentKey, index):
    """ Derive child secret key """
    return hkdfModR(parentSKToLamportPK(parentKey, index))
