from crypto.constants import TRANSACTION_FEES

fees = TRANSACTION_FEES.copy()

def get_fee(transaction_type: int, *, default: int = 0) -> int:
    """Get a fee for a given transaction type

    Args:
        transaction_type (int): transaction type for which we wish to get a fee

    Returns:
        int | None: transaction fee, or None if the transaction type is not found
    """
    return fees.get(transaction_type, default)

def set_fee(transaction_type: int, value: int) -> None:
    """Set a fee

    Args:
        transaction_type (int): transaction_type for which we wish to set a fee
        value (int): fee for a given transaction type
    """
    global fees

    fees[transaction_type] = value
