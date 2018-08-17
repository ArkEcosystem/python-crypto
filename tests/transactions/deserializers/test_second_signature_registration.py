from crypto.conf import use_network
from crypto.deserializer import Deserializer


def test_second_signature_registration():
    use_network('devnet')
    serialized = 'ff011e013bc27502034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed1920065cd1d000000000003699e966b2525f9088a6941d8d94f7869964a000efe65783d78ac82e1199fe609304402202aab49477dd3531e4473196d08fbd7c00ebb79223d5eaaeaf02c52c4041a86cf02201a7d82655f9b1d22af3ea94e6f183649bb4610cdeca3b9e20d6c8773f869831c'  # noqa
    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    assert actual.asset['signature']['publicKey'] == '03699e966b2525f9088a6941d8d94f7869964a000efe65783d78ac82e1199fe609'  # noqa
