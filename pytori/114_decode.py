# バイト列を定義（UTF-8でエンコードされた"こんにちは"）
byte_data = "こんにちは".encode("utf-8")

print("バイト列:", byte_data)

# decodeを使ってバイト列を文字列に変換
decoded_text = byte_data.decode("utf-8")

print("デコード後の文字列:", decoded_text)
