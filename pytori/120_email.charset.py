from email.charset import Charset, QP
from email.message import EmailMessage

# Charsetオブジェクトを作成（UTF-8 を指定）
charset = Charset("utf-8")

# quoted-printable でエンコードするように設定
charset.body_encoding = QP

# メールメッセージを作成
msg = EmailMessage()
msg["Subject"] = "テストメール"
msg["From"] = "sender@example.com"
msg["To"] = "receiver@example.com"

# 本文をセット（Charset を指定）
msg.set_content("これはテストメールです。特殊文字：あいうえお", charset=charset)

# 生成されたメールを出力
print(msg)
