import json
from typing import Optional

from crypto.configuration.network import get_network
from crypto.identity.address import address_from_public_key
from crypto.identity.private_key import PrivateKey
from crypto.utils.transaction_hasher import TransactionHasher

class AbstractTransaction:
    def __init__(self, data: Optional[dict] = None):
        self.data = data or {}
        self.refresh_payload_data()

    def get_payload(self) -> str:
        return ''

    def decode_payload(self, data: dict) -> Optional[dict]:
        if 'data' not in data or data['data'] == '':
            return None
        # TODO: add AbiDecoder to decode the payload
        return {}

    def refresh_payload_data(self):
        self.data['data'] = self.get_payload().lstrip('0x')

    def get_id(self) -> str:
        return self.hash(skip_signature=False).hex()

    def get_bytes(self, skip_signature: bool = False) -> bytes:
        from crypto.transactions.serializer import Serializer
        return Serializer.get_bytes(self, skip_signature)

    def sign(self, private_key: PrivateKey):
        hash_ = self.hash(skip_signature=True)
        # TODO: Implement signing logic
        return self

    def get_public_key(self, compact_signature):
        # TODO: Implement this method
        pass

    def recover_sender(self):
        compact_signature = self.get_signature()
        public_key = self.get_public_key(compact_signature)
        self.data['senderPublicKey'] = public_key.hex()
        self.data['senderAddress'] = address_from_public_key(self.data['senderPublicKey'])

    def verify(self) -> bool:
        # TODO: Implement this method
        return True

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
        # TODO: Implement this method
        pass
