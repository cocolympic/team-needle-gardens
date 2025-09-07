import errno

for name, code in errno.errorcode.items():
    print(f"{name}: {errno.errorcode[name]}")