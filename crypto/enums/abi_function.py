from enum import Enum

class AbiFunction(Enum):
    VOTE = 'vote'
    UNVOTE = 'unvote'
    VALIDATOR_REGISTRATION = 'registerValidator'
    VALIDATOR_RESIGNATION = 'resignValidator'

    def transaction_class(self):
        from crypto.transactions.types.vote import Vote
        from crypto.transactions.types.unvote import Unvote
        from crypto.transactions.types.validator_registration import ValidatorRegistration
        from crypto.transactions.types.validator_resignation import ValidatorResignation

        return {
            AbiFunction.VOTE: Vote,
            AbiFunction.UNVOTE: Unvote,
            AbiFunction.VALIDATOR_REGISTRATION: ValidatorRegistration,
            AbiFunction.VALIDATOR_RESIGNATION: ValidatorResignation
        }[self]