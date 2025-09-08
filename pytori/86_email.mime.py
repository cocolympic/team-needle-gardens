import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# 送信者と受信者の情報
from_addr = "your_email@example.com"
to_addr = "recipient@example.com"

# メールオブジェクトの作成
msg = MIMEMultipart()
msg["From"] = from_addr
msg["To"] = to_addr
msg["Subject"] = "テストメール（Python email.mime）"

# 本文を追加（プレーンテキスト）
body = "これは Python の email.mime を使ったテストメールです。"
msg.attach(MIMEText(body, "plain"))

# 添付ファイルを追加
filename = "sample.txt"  # 添付したいファイル
with open(filename, "rb") as f:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(f.read())

# Base64にエンコード
encoders.encode_base64(part)
part.add_header("Content-Disposition", f'attachment; filename="{filename}"')

# メールに添付
msg.attach(part)

try:
    server = smtplib.SMTP("smtp.example.com", 587)
    server.starttls()
    server.login(from_addr, "")
    server.sendmail(from_addr, to_addr, msg.as_string())
    print("メールを送信しました！")
except Exception as e:
    print("エラー:", e)
finally:
    server.quit()
