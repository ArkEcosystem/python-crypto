from crypto.enums.contract_abi_type import ContractAbiType
from crypto.utils.abi_base import AbiBase


def test_it_should_load_token_abi():
    abi_base = AbiBase(ContractAbiType.TOKEN)
    function_names = [
        item['name'] for item in abi_base.abi if item.get('type') == 'function'
    ]
    assert 'transfer' in function_names
    assert 'approve' in function_names
    assert 'balanceOf' in function_names
    assert 'totalSupply' in function_names
    assert 'allowance' in function_names


def test_it_should_validate_uppercase_addresses():
    assert AbiBase().is_valid_address('0xC3bBE9B1CeE1ff85Ad72b87414B0E9B7F2366763') is True

def test_it_should_validate_lowercase_addresses():
    assert AbiBase().is_valid_address('0xc3bbe9b1cee1ff85ad72b87414b0e9b7f2366763') is True
