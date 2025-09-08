import binascii

hex_str = b"48656c6c6f"
data = binascii.unhexlify(hex_str)
print(data)