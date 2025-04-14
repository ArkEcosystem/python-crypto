from crypto.utils.slot import Slot

def test_get_epoch():
    result = Slot.epoch()
    assert isinstance(result, int)

def test_get_time():
    result = Slot.time()
    assert isinstance(result, int)
