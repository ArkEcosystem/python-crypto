from crypto.utils.abi.argument_decoder import ArgumentDecoder


def test_it_should_decode_address():
    payload  = '000000000000000000000000512F366D524157BcF734546eB29a6d687B762255'
    expected = '0x512F366D524157BcF734546eB29a6d687B762255'

    decoder = ArgumentDecoder(payload)

    assert decoder.decode_address() == expected

def test_it_should_decode_unsigned_int():
    payload  = '000000000000000000000000000000000000000000000000016345785d8a0000'
    expected = 100000000000000000

    decoder = ArgumentDecoder(payload)

    assert decoder.decode_unsigned_int() == expected

def test_it_should_decode_signed_int():
    payload  = '000000000000000000000000000000000000000000000000016345785d8a0000'
    expected = 100000000000000000

    decoder = ArgumentDecoder(payload)

    assert decoder.decode_signed_int() == expected

def test_it_should_decode_bool_as_true():
    payload  = '0000000000000000000000000000000000000000000000000000000000000001'
    expected = True

    decoder = ArgumentDecoder(payload)

    assert decoder.decode_bool() == expected

def test_it_should_decode_bool_as_false():
    payload  = '0000000000000000000000000000000000000000000000000000000000000000'
    expected = False

    decoder = ArgumentDecoder(payload)

    assert decoder.decode_bool() == expected
