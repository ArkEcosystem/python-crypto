from crypto.enums.contract_abi_type import ContractAbiType
from crypto.utils.abi_decoder import AbiDecoder


def test_decode_vote_payload():
    decoder = AbiDecoder()
    function_name = 'vote'
    args = ['0x512F366D524157BcF734546eB29a6d687B762255']
    data = '0x6dd7d8ea000000000000000000000000512f366d524157bcf734546eb29a6d687b762255'

    decoded_data = decoder.decode_function_data(data)

    assert decoded_data == {
        'functionName': function_name,
        'args': args,
    }


def test_decode_token_transfer():
    decoder = AbiDecoder(ContractAbiType.TOKEN)
    data = (
        '0xa9059cbb'
        '000000000000000000000000c3bbe9b1cee1ff85ad72b87414b0e9b7f2366763'
        '00000000000000000000000000000000000000000000000000000000000003e8'
    )
    decoded = decoder.decode_function_data(data)
    assert decoded['functionName'] == 'transfer'
    assert decoded['args'] == [
        '0xC3bBE9B1CeE1ff85Ad72b87414B0E9B7F2366763',
        1000,
    ]
