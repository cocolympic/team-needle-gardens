class NullpoError(Exception):
    pass

try:
    raise NullpoError("ぬるぽ")
except NullpoError as e:
    print("ガッ！", e)