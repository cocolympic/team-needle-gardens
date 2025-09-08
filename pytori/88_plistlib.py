import plistlib
from datetime import datetime

# 書き込み用のデータを用意
data = {
    "Name": "Sample App",
    "Version": "1.0.0",
    "Enabled": True,
    "LastOpened": datetime.now(),
    "Items": ["File1", "File2", "File3"]
}

# plist ファイルに書き込み
with open("example.plist", "wb") as fp:
    plistlib.dump(data, fp)

print("example.plist を作成しました。")

# plist ファイルを読み込み
with open("example.plist", "rb") as fp:
    loaded_data = plistlib.load(fp)

print("読み込んだデータ:")
print(loaded_data)
