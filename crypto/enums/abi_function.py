from enum import Enum

class AbiFunction(Enum):
    VOTE = 'vote'
    UNVOTE = 'unvote'
    MULTIPAYMENT = 'pay'
    USERNAME_REGISTRATION = 'registerUsername'
    USERNAME_RESIGNATION = 'resignUsername'
    VALIDATOR_REGISTRATION = 'registerValidator'
    VALIDATOR_RESIGNATION = 'resignValidator'
    UPDATE_VALIDATOR = 'updateValidator'
    TRANSFER = 'transfer'
    APPROVE = 'approve'
    BATCH_TRANSFER_FROM = 'batchTransferFrom'
