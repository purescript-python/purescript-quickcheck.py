import struct

def float32ToInt32(n):
    return struct.unpack("i", struct.pack("f", n))
