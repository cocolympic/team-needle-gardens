import shelve

# 保存
with shelve.open("mydata") as db:
    db["msg"] = "Hello"

# 読み込み
with shelve.open("mydata") as db:
    print(db["msg"])