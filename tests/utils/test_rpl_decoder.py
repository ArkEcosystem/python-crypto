from crypto.utils.rlp_decoder import RlpDecoder


def test_decode_function_call(load_transaction_fixture):
    fixture = load_transaction_fixture('transactions/transfer')

    decoded_rlp = RlpDecoder.decode('0x' + fixture['serialized'])

    assert len(decoded_rlp) == 9
    assert decoded_rlp[0] == '0x01'
    assert decoded_rlp[1] == '0x012a05f200'
    assert decoded_rlp[2] == '0x5208'
    assert decoded_rlp[3] == '0x6f0182a0cc707b055322ccf6d4cb6a5aff1aeb22'
    assert decoded_rlp[4] == '0x05f5e100'
    assert decoded_rlp[5] == '0x'
    assert decoded_rlp[6] == '0x5c6b'
    assert decoded_rlp[7] == '0xa1f79cb40a4bb409d6cebd874002ceda3ec0ccb614c1d8155f5c2f7f798135f9'
    assert decoded_rlp[8] == '0x2d2ef517aaf6feed747385e260c206f46b2ce9d6b2a585427a111685a097bd79'

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
