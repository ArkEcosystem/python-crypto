from datetime import datetime

from crypto.utils.slot import get_epoch, get_time


def test_get_epoch():
    result = get_epoch()
    assert isinstance(result, datetime)


def test_get_time():
    result = get_time()
    assert isinstance(result, int)
