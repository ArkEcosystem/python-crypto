from crypto.utils.abi_encoder import AbiEncoder


def test_encode_vote_function_call():
    encoder = AbiEncoder()
    function_name = 'vote'
    args = ['0x512F366D524157BcF734546eB29a6d687B762255']
    expected_encoded_data = '0x6dd7d8ea000000000000000000000000512f366d524157bcf734546eb29a6d687b762255'

    encoded_data = encoder.encode_function_call(function_name, args)

    assert encoded_data == expected_encoded_data
