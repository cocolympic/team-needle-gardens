from email.message import EmailMessage
from email import policy
import smtplib

# EmailMessage を作成（utf-8 を扱いやすい default policy を利用）
msg = EmailMessage(policy=policy.default)
msg['From'] = "sender@example.com"
msg['To'] = "receiver@example.com"
msg['Subject'] = "テストメール（policy.default 使用）"

# 本文を設定（UTF-8で自動エンコードされる）
msg.set_content("これは email.policy を使ったテストメールです。\n改行やエンコードが自動で処理されます。")

# メールの内容を表示
print("----- メールの内容（生成結果） -----")
print(msg)
