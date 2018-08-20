from datetime import datetime

from crypto.conf import use_network
from crypto.utils.slot import get_epoch, get_time


def test_get_epoch():
    use_network('devnet')
    result = get_epoch()
    assert isinstance(result, datetime)


def test_get_time():
    use_network('devnet')
    result = get_time()
    assert isinstance(result, int)
