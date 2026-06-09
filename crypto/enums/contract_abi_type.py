from enum import Enum

class ContractAbiType(Enum):
    CUSTOM = 'custom'
    CONSENSUS = 'consensus'
    MULTIPAYMENT = 'multipayment'
    TOKEN = 'token'
    USERNAMES = 'usernames'
    ERC20BATCH_TRANSFER = 'erc20BatchTransfer'
