from enum import Enum

class AbiFunction(Enum):
    VOTE = 'vote'
    UNVOTE = 'unvote'
    VALIDATOR_REGISTRATION = 'registerValidator'
    VALIDATOR_RESIGNATION = 'resignValidator'
