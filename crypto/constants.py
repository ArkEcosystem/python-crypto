from enum import Enum


class TransactionTypes(Enum):
    transfer = 0
    second_signature_registration = 1
    delegate_registration = 2
    vote = 3
    multi_signature_registration = 4
    ipfs = 5
    timelock_transfer = 6
    multi_payment = 7
    delegate_resignation = 8


class TransactionFees(Enum):
    transfer = 10000000
    second_signature_registration = 500000000
    delegate_registration = 2500000000
    vote = 100000000
    multi_signature_registration = 500000000
    ipfs = 0
    timelock_transfer = 0
    multi_payment = 0
    delegate_resignation = 0
