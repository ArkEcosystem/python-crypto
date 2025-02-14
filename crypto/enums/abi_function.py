from enum import Enum

class AbiFunction(Enum):
    VOTE = 'vote'
    UNVOTE = 'unvote'
    USERNAME_REGISTRATION = 'registerUsername'
    USERNAME_RESIGNATION = 'resignUsername'
    VALIDATOR_REGISTRATION = 'registerValidator'
    VALIDATOR_RESIGNATION = 'resignValidator'
