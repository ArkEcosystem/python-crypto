from crypto.utils.rlp_decoder import RlpDecoder


def test_decode_function_call(load_transaction_fixture):
    fixture = load_transaction_fixture('transfer')

    decoded_rlp = RlpDecoder.decode('0x' + fixture['serialized'][2:])

    assert len(decoded_rlp) == 12
    assert decoded_rlp[0] == '0x2710'
    assert decoded_rlp[1] == '0x01'
    assert decoded_rlp[2] == '0x'
    assert decoded_rlp[3] == '0x012a05f200'
    assert decoded_rlp[4] == '0x5208'
    assert decoded_rlp[5] == '0x6f0182a0cc707b055322ccf6d4cb6a5aff1aeb22'
    assert decoded_rlp[6] == '0x05f5e100'
    assert decoded_rlp[7] == '0x'
    assert decoded_rlp[8] == []
    assert decoded_rlp[9] == '0x01'
    assert decoded_rlp[10] == '0x104665257d4dea61c4654e74c6c0f6cd0a398905781c3040bea67dc641a66da0'
    assert decoded_rlp[11] == '0x46d718d04b2331f3b0561808549ed3f3f0d867a284acf6b334869078df7a9136'

def test_decoding_str():
    decoded = RlpDecoder.decode('0x8774657374696e67')

    assert decoded == '0x74657374696e67'

def test_decoding_bytes():
    decoded = RlpDecoder.decode('0x8774657374696e67')

    assert decoded == '0x74657374696e67'

def test_decoding_list():
    decoded = RlpDecoder.decode('0xc88774657374696e67')

    assert decoded == ['0x74657374696e67']

def test_decoding_int():
    decoded = RlpDecoder.decode('0x86313233343536')

    assert decoded == '0x313233343536'
