from crypto.message import sign_message, verify_message


def test_signing_and_verifying_a_message(message):
    data = sign_message(message['data']['message'].encode(), message['passphrase'].encode())
    signature = data['signature']
    public_key = data['public_key']

    assert verify_message(message['data']['signature'].encode(), public_key, signature) is True
