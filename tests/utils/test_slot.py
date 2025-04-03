from datetime import datetime

from crypto.utils.slot import Slot

def test_get_epoch():
    result = Slot.epoch()
    assert isinstance(result, datetime)

def test_get_time():
    result = Slot.time()
    assert isinstance(result, int)
