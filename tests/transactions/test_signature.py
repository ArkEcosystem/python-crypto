from crypto.transactions.builder.transfer import Transfer
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

def test_transfer_transaction():
    transaction = Transfer(
        recipientId='0xb693449AdDa7EFc015D87944EAE8b7C37EB1690A',
        amount=1,
        fee=10000000
    )
    transaction.set_type_group(1)
    transaction.set_nonce(1)
    transaction.sign('my super secret passphrase')

    isVerified = Signature.verify(
        bytes.fromhex('d07662b9a917f158a7ad8431aff8b31a70fe3a7af562db3ead41e7b5e00b7d9a27b3faf26699096baddbb45b2f1c3b0aa180301b001e19b8eaeb4e13055eaa0c'),
        transaction.transaction.to_bytes(),
        bytes.fromhex('023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3'),
    )

    assert isVerified == True
