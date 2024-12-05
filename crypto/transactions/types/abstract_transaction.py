import json
from typing import Optional

from crypto.configuration.network import get_network
from crypto.identity.address import address_from_public_key
from crypto.identity.private_key import PrivateKey
from crypto.utils.transaction_hasher import TransactionHasher
from coincurve import PublicKey
from crypto.utils.abi_decoder import AbiDecoder

class AbstractTransaction:
    def __init__(self, data: Optional[dict] = None):
        self.data = data or {}
        self.refresh_payload_data()

    def get_payload(self) -> str:
        return ''

    def decode_payload(self, data: dict) -> Optional[dict]:
        if 'data' not in data or data['data'] == '':
            return None
        
        payload = data['data']
        decoder = AbiDecoder()

        decoded_data = decoder.decode_function_data(payload)

        return decoded_data

    def refresh_payload_data(self):
        self.data['data'] = self.get_payload().lstrip('0x')

    def get_id(self) -> str:
        return self.hash(skip_signature=False).hex()

    def get_bytes(self, skip_signature: bool = False) -> bytes:
        from crypto.transactions.serializer import Serializer
        return Serializer.get_bytes(self, skip_signature)

    def sign(self, private_key: PrivateKey):
        hash_ = self.hash(skip_signature=True)
        signature_with_recid = private_key.private_key.sign_recoverable(hash_, hasher=None)
        signature_hex = signature_with_recid.hex()
        self.data['signature'] = signature_hex
        return self

    def get_public_key(self, compact_signature, hash_):
        public_key = PublicKey.from_signature_and_message(compact_signature, hash_, hasher=None)
        return public_key

    def recover_sender(self):
        signature_hex = self.data.get('signature')
        if not signature_hex:
            raise ValueError("No signature to recover from")

        signature_with_recid = bytes.fromhex(signature_hex)
        hash_ = self.hash(skip_signature=True)
        public_key = self.get_public_key(signature_with_recid, hash_)
        self.data['senderPublicKey'] = public_key.format().hex()
        self.data['senderAddress'] = address_from_public_key(self.data['senderPublicKey'])

    def verify(self) -> bool:
        signature_hex = self.data.get('signature')
        if not signature_hex:
            return False

        signature_with_recid = bytes.fromhex(signature_hex)
        hash_ = self.hash(skip_signature=True)
        recovered_public_key = self.get_public_key(signature_with_recid, hash_)
        sender_public_key_hex = self.data.get('senderPublicKey')
        if not sender_public_key_hex:
            return False

        sender_public_key_bytes = bytes.fromhex(sender_public_key_hex)
        return recovered_public_key.format() == sender_public_key_bytes

    def serialize(self, skip_signature: bool = False) -> bytes:
        from crypto.transactions.serializer import Serializer
        return Serializer(self).serialize(skip_signature)

    def to_dict(self) -> dict:
        return {k: v for k, v in self.data.items() if v is not None}

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def hash(self, skip_signature: bool) -> bytes:
        hash_data = self.data.copy()
        if skip_signature:
            hash_data['signature'] = None
        return TransactionHasher.to_hash(hash_data, skip_signature)

    def get_signature(self):
        signature_hex = self.data.get('signature')
        if signature_hex:
            return bytes.fromhex(signature_hex)
        return None
