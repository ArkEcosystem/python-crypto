from crypto.message import sign_message, verify_message


def test_signing_and_verifying_a_message():
    message = 'hello world'.encode()
    secret = 'top secret yo'.encode()

    data = sign_message(message, secret)

    signature = data['signature']
    public_key = data['public_key']
    assert verify_message(message, public_key, signature) is True
