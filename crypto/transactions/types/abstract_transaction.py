import json
from typing import Optional

from crypto.configuration.network import get_network
from crypto.identity.address import address_from_public_key
from crypto.transactions.serializer import Serializer
# @todo add TransactionHasher
# from crypto.utils.transaction_hasher import TransactionHasher
from crypto.identity.private_key import PrivateKey


class AbstractTransaction:
    def __init__(self, data: Optional[dict] = None):
        self.data = data or {}
        self.refresh_payload_data()

    def get_payload(self) -> str:
        return ''

    def decode_payload(self, data: dict) -> Optional[dict]:
        if 'data' not in data:
            return None

        payload = data['data']

        if payload == '':
            return None

        # @TODO: add abidecoder
        return {}

    def refresh_payload_data(self):
        self.data['data'] = self.get_payload().lstrip('0x')

    def get_id(self) -> str:
        return self.hash(skip_signature=False).hex()

    def get_bytes(self, skip_signature: bool = False) -> bytes:
        return Serializer.get_bytes(self, skip_signature)

    def sign(self, private_key: PrivateKey):
        hash_ = self.hash(skip_signature=True)
        # signature = private_key.sign_compact(hash_)
        # # Extraer el recovery ID y la firma
        # recovery_id = signature[0] - 27 - 4
        # signature_hex = signature[1:].hex()
        # # Añadir el recovery ID al final
        # signature_hex += format(recovery_id, '02x')
        # self.data['signature'] = signature_hex


        return self

    def get_public_key(self, compact_signature):
        # @TODO: Implementar este método
        pass

    def recover_sender(self):
        compact_signature = self.get_signature()
        public_key = self.get_public_key(compact_signature)
        self.data['senderPublicKey'] = public_key.hex()
        self.data['senderAddress'] = address_from_public_key(self.data['senderPublicKey'])

    def verify(self) -> bool:
        # @TODO: Implment this method
        return True  # temporary

    def serialize(self, skip_signature: bool = False) -> bytes:
        return Serializer(self).serialize(skip_signature)

    def to_dict(self) -> dict:
        return {k: v for k, v in self.data.items() if v is not None}

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def hash(self, skip_signature: bool) -> bytes:
        hash_data = {
            'gasPrice': self.data.get('gasPrice'),
            'network': self.data.get('network', get_network().get('version')),
            'nonce': self.data.get('nonce'),
            'value': self.data.get('value'),
            'gasLimit': self.data.get('gasLimit'),
            'data': self.data.get('data'),
            'recipientAddress': self.data.get('recipientAddress'),
            'signature': self.data.get('signature') if not skip_signature else None,
        }
        
        # @TODO: add transaction hasher
        # return TransactionHasher.to_hash(hash_data, skip_signature)
        return b''

    def get_signature(self):
        # @TODO: implement this
        pass
