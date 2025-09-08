from email.header import Header, decode_header

# 日本語を含む件名をエンコード
subject = Header("こんにちは世界", "utf-8")
print(subject)