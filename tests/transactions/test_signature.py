from crypto.transactions.signature import Signature

def test_should_sign_and_verify():
    isVerified = Signature.verify(
        bytes.fromhex(
            Signature.sign(
                bytes.fromhex("814857ce48e291893feab95df02e1dbf7ad3994ba46f247f77e4eefd5d8734a2"),
                bytes.fromhex("814857ce48e291893feab95df02e1dbf7ad3994ba46f247f77e4eefd5d8734a2"),
            ),
				),
				bytes.fromhex('814857ce48e291893feab95df02e1dbf7ad3994ba46f247f77e4eefd5d8734a2'),
				bytes.fromhex('e84093c072af70004a38dd95e34def119d2348d5261228175d032e5f2070e19f'),
    )

    assert isVerified == True

def test_should_sign_and_verify_with_ecdsa_key_with_prefix():
    isVerified = Signature.verify(
        bytes.fromhex(
            Signature.sign(
                bytes.fromhex("6616cd071ecbfe525be817d29eb1ccd6d93af0a9207356b38dcd73fcc84ff297"),
                bytes.fromhex("6acdb0def03305800b75e9c020e0a9b0504a543f56253f694ff35f1dce8a193f"),
            ),
				),
				bytes.fromhex('6616cd071ecbfe525be817d29eb1ccd6d93af0a9207356b38dcd73fcc84ff297'),
				bytes.fromhex('025f7362e1baff21b8441c20b3f54583eb2f5925afada140b5a95880a2224a9d48'),
    )

    assert isVerified == True

def test_should_sign_and_verify_with_ecdsa_key_without_prefix():
    isVerified = Signature.verify(
        bytes.fromhex(
            Signature.sign(
                bytes.fromhex("6616cd071ecbfe525be817d29eb1ccd6d93af0a9207356b38dcd73fcc84ff297"),
                bytes.fromhex("6acdb0def03305800b75e9c020e0a9b0504a543f56253f694ff35f1dce8a193f"),
            ),
				),
				bytes.fromhex('6616cd071ecbfe525be817d29eb1ccd6d93af0a9207356b38dcd73fcc84ff297'),
				bytes.fromhex('5f7362e1baff21b8441c20b3f54583eb2f5925afada140b5a95880a2224a9d48'),
    )

    assert isVerified == True

def test_should_not_sign_and_verify_with_wrong_ecdsa_key():
    isVerified = Signature.verify(
        bytes.fromhex(
            Signature.sign(
                bytes.fromhex("6616cd071ecbfe525be817d29eb1ccd6d93af0a9207356b38dcd73fcc84ff297"),
                bytes.fromhex("6acdb0def03305800b75e9c020e0a9b0504a543f56253f694ff35f1dce8a193f"),
            ),
				),
				bytes.fromhex('6616cd071ecbfe525be817d29eb1ccd6d93af0a9207356b38dcd73fcc84ff297'),
				bytes.fromhex('02d076ae01c84ad5e72eb2aae9a3c60784b08cc1f0e8624fe3cc51648a163ee120'),
    )

    assert isVerified == False
