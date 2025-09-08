import struct

data = (1, 2, 3)
b = struct.pack("iii", *data)  # 3つの整数をまとめてバイト列に
print(b)

nums = struct.unpack("iii", b)
print(nums)