from enum import Enum

class ContractAbiType(Enum):
    CUSTOM = 'custom'
    CONSENSUS = 'consensus'
    MULTIPAYMENT = 'multipayment'
    TOKEN = 'token'
    USERNAMES = 'usernames'
