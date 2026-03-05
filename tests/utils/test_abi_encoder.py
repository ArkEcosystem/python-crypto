from crypto.enums.contract_abi_type import ContractAbiType
from crypto.utils.abi_encoder import AbiEncoder


def test_encode_vote_function_call():
    encoder = AbiEncoder()
    function_name = 'vote'
    args = ['0x512F366D524157BcF734546eB29a6d687B762255']
    expected_encoded_data = '0x6dd7d8ea000000000000000000000000512f366d524157bcf734546eb29a6d687b762255'

    encoded_data = encoder.encode_function_call(function_name, args)

    assert encoded_data == expected_encoded_data

def test_encode_address():
    assert AbiEncoder().encode_address('0xC3bBE9B1CeE1ff85Ad72b87414B0E9B7F2366763') == {
        'dynamic': False,
        'encoded': '0x000000000000000000000000c3bbe9b1cee1ff85ad72b87414b0e9b7f2366763',
    }

    # lowercase
    assert AbiEncoder().encode_address('0xc3bbe9b1cee1ff85ad72b87414b0e9b7f2366763') == {
        'dynamic': False,
        'encoded': '0x000000000000000000000000c3bbe9b1cee1ff85ad72b87414b0e9b7f2366763',
    }


def test_encode_token_transfer():
    encoder = AbiEncoder(ContractAbiType.TOKEN)
    encoded = encoder.encode_function_call(
        'transfer',
        ['0xC3bBE9B1CeE1ff85Ad72b87414B0E9B7F2366763', 1000]
    )
    expected = (
        '0xa9059cbb'
        '000000000000000000000000c3bbe9b1cee1ff85ad72b87414b0e9b7f2366763'
        '00000000000000000000000000000000000000000000000000000000000003e8'
    )
    assert encoded == expected
