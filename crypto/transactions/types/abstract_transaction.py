import json
from typing import Optional

from crypto.enums.constants import Constants
from crypto.enums.contract_abi_type import ContractAbiType
from crypto.identity.address import address_from_public_key
from crypto.identity.private_key import PrivateKey
from crypto.utils.transaction_utils import TransactionUtils
from coincurve import PublicKey

class AbstractTransaction:
    def __init__(self, data: dict):
        self.data = data
        self.refresh_payload_data()

    def get_payload(self) -> str:
        return ''

    def refresh_payload_data(self):
        self.data['data'] = TransactionUtils.parse_hex_from_str(self.get_payload())

    def get_id(self) -> str:
        return TransactionUtils.get_id(self.data)

    def sign(self, private_key: PrivateKey):
        transaction_hash = TransactionUtils.to_buffer(self.data, skip_signature=True).decode()

        message = bytes.fromhex(transaction_hash)

        transaction_signature = private_key.sign(message)

        self.data['v'] = transaction_signature[0]
        self.data['r'] = transaction_signature[1:33].hex()
        self.data['s'] = transaction_signature[33:].hex()

        return self

    def get_public_key(self, compact_signature, hash_):
        public_key = PublicKey.from_signature_and_message(compact_signature, hash_, hasher=None)

        return public_key

    def recover_sender(self):
        signature_with_recid = self.get_signature()
        if not signature_with_recid:
            return False

        hash_ = bytes.fromhex(self.hash(skip_signature=True))
        public_key = self.get_public_key(signature_with_recid, hash_)
        self.data['senderPublicKey'] = public_key.format().hex()
        self.data['senderAddress'] = address_from_public_key(self.data['senderPublicKey'])

    def verify(self) -> bool:
        signature_with_recid = self.get_signature()
        if not signature_with_recid:
            return False

        hash_ = bytes.fromhex(self.hash(skip_signature=True))
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

    def hash(self, skip_signature: bool) -> str:
        return TransactionUtils.to_hash(self.data, skip_signature=skip_signature)

    def get_signature(self):
        recover_id = int(self.data.get('v', 0)) - Constants.ETHEREUM_RECOVERY_ID_OFFSET.value
        r = self.data.get('r')
        s = self.data.get('s')

        if r and s:
            return bytes.fromhex(r) + bytes.fromhex(s) + bytes([recover_id])

        return None

    @staticmethod
    def decode_payload(data: dict, abi_type: ContractAbiType = ContractAbiType.CONSENSUS) -> Optional[dict]:
        from crypto.transactions.deserializer import Deserializer

        return Deserializer.decode_payload(data, abi_type)
