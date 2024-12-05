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
