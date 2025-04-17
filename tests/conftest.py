import pytest
import json
import os
from crypto.configuration.network import Network
from crypto.networks.testnet import Testnet


@pytest.fixture(scope='session', autouse=True)
def configure_network():
    """
    Configures the network to Testnet before running any tests.
    This fixture runs automatically once per test session.
    """
    Network.set_network(Testnet())

@pytest.fixture
def load_transaction_fixture():
    """
    Fixture to load a transaction fixture from the fixtures directory.

    Usage in tests:
        def test_example(load_transaction_fixture):
            fixture = load_transaction_fixture('fixture_name')
    """
    def _load_transaction_fixture(fixture_name):
        fixtures_path = os.path.join(
            os.path.dirname(__file__),
            './fixtures',
            f'{fixture_name}.json'
        )
        with open(fixtures_path, 'r') as f:
            return json.load(f)
    return _load_transaction_fixture

@pytest.fixture
def passphrase():
    """Passphrase used for tests"""

    return 'found lobster oblige describe ready addict body brave live vacuum display salute lizard combine gift resemble race senior quality reunion proud tell adjust angle'

@pytest.fixture
def transaction_type_0():
    """Transaction of type "transfer"
    """
    data = {
        "version": 1,
        "network": 30,
        "typeGroup": 1,
        "type": 0,
        "nonce": 5,
        "senderPublicKey": '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3',
        "fee": 10000000,
        "amount": 1,
        "expiration": 0,
        "to": '0xb693449AdDa7EFc015D87944EAE8b7C37EB1690A',
        "signature": '95abbcadcfb4b8991392b1ce819777abd471d837ae8bfbf28f39cad4c7b2e815116622f3ceb099386ec19b781d7b38bdf008e1851a7f848bb88382f893ff85ea',
        "hash": '0ba2a3bf50747a89e5527235ec9beaab055ceadedfa347e81e95ba97e5166c6b',
        "serialized": "ff011e0100000000000500000000000000023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3809698000000000000010000000000000000000000b693449adda7efc015d87944eae8b7c37eb1690a95abbcadcfb4b8991392b1ce819777abd471d837ae8bfbf28f39cad4c7b2e815116622f3ceb099386ec19b781d7b38bdf008e1851a7f848bb88382f893ff85ea",
    }
    return data


@pytest.fixture
def transaction_type_2():
    """Transaction of type "validator registration"
    """
    data = {
        'version': 1,
        'network': 30,
        'typeGroup': 1,
        'type': 2,
        'nonce': 5,
        'senderPublicKey': '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3',
        'fee': 2500000000,
        'asset': {
            'validatorPublicKey': 'a08058db53e2665c84a40f5152e76dd2b652125a6079130d4c315e728bcf4dd1dfb44ac26e82302331d61977d3141118'
        },
        'signature': '5a1a0dba931a1b0a9055801578109a657fd4a2551fdb42dfd24a2c3a70835648d576f1d6b76b7a1cfedb4061d877c0a0f8adb3b47c7bbcb43b1b038da6b3ab19',  # noqa
        'amount': 0,
        'hash': '89b3df28b9069b9cba26ba8a4d2b970bb7e87a37271a96a0e9e0dd831e831f8d',
        'serialized': 'ff011e0100000002000500000000000000023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d300f902950000000000a08058db53e2665c84a40f5152e76dd2b652125a6079130d4c315e728bcf4dd1dfb44ac26e82302331d61977d31411185a1a0dba931a1b0a9055801578109a657fd4a2551fdb42dfd24a2c3a70835648d576f1d6b76b7a1cfedb4061d877c0a0f8adb3b47c7bbcb43b1b038da6b3ab19'  # noqa
    }
    return data


@pytest.fixture
def transaction_type_3():
    """Transaction of type "vote"
    """
    data = {
        "version": 1,
        "network": 30,
        "typeGroup": 1,
        "type": 3,
        "nonce": 5,
        "senderPublicKey": "023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3",
        "fee": 100000000,
        "asset": {
            "unvotes": [],
            "votes": ["03f25455408f9a7e6c6a056b121e68fbda98f3511d22e9ef27b0ebaf1ef9e4eabc"]
        },
        "signature": "5946eea46e46026bd5feb5335ba9411fa30677c9a9a9a788065cf1e95bf2896659485fd26b78613640b1209827ce6d4587a05a4721c63e8af24d3351e1eeaa6c",  # noqa
        "amount": 0,
        "hash": "a2ff7837281cb978d6f293b46da7bb0342fe09923eede0bfbef9dd57ffee9158",
        "serialized":
        "ff011e0100000003000500000000000000023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d300e1f50500000000000103f25455408f9a7e6c6a056b121e68fbda98f3511d22e9ef27b0ebaf1ef9e4eabc005946eea46e46026bd5feb5335ba9411fa30677c9a9a9a788065cf1e95bf2896659485fd26b78613640b1209827ce6d4587a05a4721c63e8af24d3351e1eeaa6c"  # noqa
    }
    return data


@pytest.fixture
def transaction_type_4():
    """Transaction of type "multi signature registration"
    """
    data = {
        'version': 1,
        'network': 30,
        'typeGroup': 1,
        'type': 4,
        'nonce': 5,
        'senderPublicKey': '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3',
        'hash': 'f140e52f89c3b782da2fc47111abc85610e784ab3a55115712fe5fb2aa061f16',
        'amount': 0,
        'fee': 500000000,
        'signature': '5cc5dc6ca87dd1b3bd24dba27e72cce6b32284821f217f1a0195ba319e3ad3b8c9bdae225da62cd52ee911e7ffecd5e4d1197421070a8c92ee57e00398cf3dcb',  # noqa
        'asset': {
            'multiSignature': {
                'publicKeys': [
                    "029fab3cb2f5e248ae7cbb4de646741da4d73c493b2a03ab5c71507fb2c0dcca92",
                    "03629f9dbf7f1e91cefa845126189816ceae357bdd1f41bd14787318a7d5b55d48",
                    "027941d2059f89a26d89e87d3385e261a0ede1234aaeaa487012b69d6b67962dc5",
                ],
                'min': 2,
            }
        },
        'signatures': [
            '003eeb63ff599b2d2255127323522f0559dd9444873b08203f998515bfb107cee68edb9e393622d93913a1afdb28768d6accd2b725c75942a638719795de344156',  # noqa
            '017aeccd6d60ae1b6ab5121f59225fe8246d58f8cfae76deb3e492a87abe4e37f622cc07948f7c9b62c0447deef05f4960bae25354699f9d8f9ddfa4be4de04923',  # noqa
            '02e6df01f999919f1a6236c8ac8ce54e3e41042e14547b1aa86b44c4c05e02f1ac89a44d0ad8a5f0374b00b5285d0b9b1cb64e4212a792bf5e4775c4d761c44c9d'  # noqa
        ],
        'serialized': 'ff011e0100000004000500000000000000023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d30065cd1d00000000000203029fab3cb2f5e248ae7cbb4de646741da4d73c493b2a03ab5c71507fb2c0dcca9203629f9dbf7f1e91cefa845126189816ceae357bdd1f41bd14787318a7d5b55d48027941d2059f89a26d89e87d3385e261a0ede1234aaeaa487012b69d6b67962dc55cc5dc6ca87dd1b3bd24dba27e72cce6b32284821f217f1a0195ba319e3ad3b8c9bdae225da62cd52ee911e7ffecd5e4d1197421070a8c92ee57e00398cf3dcb003eeb63ff599b2d2255127323522f0559dd9444873b08203f998515bfb107cee68edb9e393622d93913a1afdb28768d6accd2b725c75942a638719795de344156017aeccd6d60ae1b6ab5121f59225fe8246d58f8cfae76deb3e492a87abe4e37f622cc07948f7c9b62c0447deef05f4960bae25354699f9d8f9ddfa4be4de0492302e6df01f999919f1a6236c8ac8ce54e3e41042e14547b1aa86b44c4c05e02f1ac89a44d0ad8a5f0374b00b5285d0b9b1cb64e4212a792bf5e4775c4d761c44c9d'  # noqa
    }
    return data


@pytest.fixture
def transaction_type_6():
    """Transaction of type "multi payment"
    """
    data = {
        'version': 1,
        'network': 30,
        'typeGroup': 1,
        'type': 6,
        'nonce': 5,
        'senderPublicKey': '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3',
        'fee': 10000000,
        'amount': 0,
        'asset': {
            'payments': [
                {
                    'amount': 100000000,
                    'recipientId': '0xb693449AdDa7EFc015D87944EAE8b7C37EB1690A'
                },
                {
                    'amount': 200000000,
                    'recipientId': '0xb693449AdDa7EFc015D87944EAE8b7C37EB1690A'
                },
            ],
        },
        'signature': '220b5d1597716c63f7945da495793f6fcb9997481108e9c1e4e7b72c6ec31fe11b2015b4940938ca8979e84ec06550825b3c0a24e23fdae087173d4d74e4d8bc',
        'hash': 'c42df7851d62e99ef52363b6344a7f81069e5a2e239144853990839aa4084fb3',
        'serialized': 'ff011e0100000006000500000000000000023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3809698000000000000020000e1f50500000000b693449adda7efc015d87944eae8b7c37eb1690a00c2eb0b00000000b693449adda7efc015d87944eae8b7c37eb1690a220b5d1597716c63f7945da495793f6fcb9997481108e9c1e4e7b72c6ec31fe11b2015b4940938ca8979e84ec06550825b3c0a24e23fdae087173d4d74e4d8bc'
    }
    return data


@pytest.fixture
def transaction_type_7():
    """Transaction of type "validator resignation"
    """
    data = {
        'version': 1,
        'network': 30,
        'typeGroup': 1,
        'type': 7,
        'nonce': 5,
        'senderPublicKey': '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3',
        'fee': 2500000000,
        'amount': 0,
        'signature': '34ec032ec41273043cf4f809e16e0892104743fac7da1d7ff33fb75b5569cc1c59e03558ceb2f28daf1cfaec8b88ce994c2114177f4bfeca03c0b0533d58dc1f',
        'hash': '4579323b640090f5a43f1b22d29082348a6f0016b2b28ad3bc44f1838647c83d',
        'serialized': 'ff011e0100000007000500000000000000023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d300f90295000000000034ec032ec41273043cf4f809e16e0892104743fac7da1d7ff33fb75b5569cc1c59e03558ceb2f28daf1cfaec8b88ce994c2114177f4bfeca03c0b0533d58dc1f'
    }
    return data


@pytest.fixture
def transaction_type_8():
    """Transaction of type "username registration"
    """
    data = {
        'version': 1,
        'network': 30,
        'typeGroup': 1,
        'type': 8,
        'nonce': 9,
        'senderPublicKey': '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3',
        'fee': 2500000000,
        'asset': {
            'username': 'test_username'
        },
        'signature': 'd6886e48b8df120f5f51d22c00583ef9cda61c32fd578cd07812f95cca16cdf98972e7f0789221cf1e0ad8fe174f68b4b3fe57a32692c83e0f7b1bd18c9b1640',  # noqa
        'amount': 0,
        'hash': 'f6ae0049bc3b79ddac96e37ceb6dadbf311b817d70ae1613ca5a97ceba6c8d40',
        'serialized': 'ff011e0100000008000900000000000000023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d300f9029500000000000d746573745f757365726e616d65d6886e48b8df120f5f51d22c00583ef9cda61c32fd578cd07812f95cca16cdf98972e7f0789221cf1e0ad8fe174f68b4b3fe57a32692c83e0f7b1bd18c9b1640'  # noqa
    }
    return data


@pytest.fixture
def transaction_type_9():
    """Transaction of type "username resignation"
    """
    data = {
        'version': 1,
        'network': 30,
        'typeGroup': 1,
        'type': 9,
        'nonce': 9,
        'senderPublicKey': '023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d3',
        'fee': 2500000000,
        'amount': 0,
        'signature': '728c2c5d5f090e8c5dfd433bb2b15b30442cbafb9b882117f7b6f284da4093c6a96e8456f764628ec809514ac4e8b06d5450978b9b763f7d01f696b8881f702a',
        'hash': '9d01eb12cb47d5acbfe0ba0aff501e24e8313e2b08ecba118bb45332903d776b',
        'serialized': 'ff011e0100000009000900000000000000023efc1da7f315f3c533a4080e491f32cd4219731cef008976c3876539e1f192d300f902950000000000728c2c5d5f090e8c5dfd433bb2b15b30442cbafb9b882117f7b6f284da4093c6a96e8456f764628ec809514ac4e8b06d5450978b9b763f7d01f696b8881f702a'
    }
    return data
