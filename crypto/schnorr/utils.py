import re
import binascii
import sys


PY3 = True if sys.version_info[0] >= 3 else False

if PY3:
    import io
    BytesIO = io.BytesIO
else:
    from cStringIO import StringIO
    BytesIO = StringIO

HEX = re.compile("^[0-9a-fA-F]$")
BHEX = re.compile(b"^[0-9a-fA-F]$")


def hexlify(data):
    if PY3 and isinstance(data, str):
        if HEX.match(data):
            return data
        else:
            data = data.encode()
    result = binascii.hexlify(data)
    return str(result.decode() if isinstance(result, bytes) else result)

def unhexlify(data):
    if PY3 and isinstance(data, bytes):
        if BHEX.match(data):
            data = data.decode()
        else:
            return data
    if len(data) % 2:
        data = "0" + data
    result = binascii.unhexlify(data)
    return result if isinstance(result, bytes) else result.encode()
