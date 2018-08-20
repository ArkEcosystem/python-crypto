from crypto.conf import use_network
from crypto.transactions.deserializer import Deserializer


def test_delegate_registration_deserializer():
    use_network('devnet')
    serialized = 'ff011e02a5b87502034151a3ec46b5670a682b0a63394f863587d1bc97483b1b6c70eb58e7f0aed19200f90295000000000009626f6c646e696e6a61304402205fe105d2d23b66d2dbae3bd12bc0d1df498936a7614c71c0481bbf5159ad8d2002201084f5c24e802964b3075ac6feac91429c356c960a5faa8ef3c397a4b25c299a'  # noqa
    deserializer = Deserializer(serialized)
    actual = deserializer.deserialize()
    assert actual.asset['delegate'] == {'username': 'boldninja'}
