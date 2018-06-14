from crypto.constants import TRANSACTION_FEES

fees = TRANSACTION_FEES.copy()


def get_fee(transaction_type):
    """Get a fee for a given transaction type

    Args:
        transaction_type (int): transaction type for which we wish to get a fee

    Returns:
        int: transaction fee
    """
    return fees.get(transaction_type)


def set_fee(transaction_type, value):
    """Set a fee

    Args:
        transaction_type (int): transaction_type for which we wish to set a fee
        value (int): fee for a given transaction type
    """
    global fees
    fees[transaction_type] = value
