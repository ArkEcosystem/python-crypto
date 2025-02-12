from crypto.utils.rlp_decoder import RlpDecoder


def test_decode_function_call(load_transaction_fixture):
    fixture = load_transaction_fixture('transfer')

    decoded_rlp = RlpDecoder.decode('0x' + fixture['serialized'][2:])

    assert len(decoded_rlp) == 12
    assert decoded_rlp[0] == '0x1e'
    assert decoded_rlp[1] == '0x01'
    assert decoded_rlp[2] == '0x'
    assert decoded_rlp[3] == '0x05'
    assert decoded_rlp[4] == '0x5208'
    assert decoded_rlp[5] == '0x6f0182a0cc707b055322ccf6d4cb6a5aff1aeb22'
    assert decoded_rlp[6] == '0x05f5e100'
    assert decoded_rlp[7] == '0x'
    assert decoded_rlp[8] == []
    assert decoded_rlp[9] == '0x'
    assert decoded_rlp[10] == '0x0567c4def813a66e03fa1cd499a27c6922698a67e25e0b38458d8f4bb0e581fc'
    assert decoded_rlp[11] == '0x25fcdf9d110b82bde15bae4a49118deb83cfc3ec1656c2a29286d7836d328abe'

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
