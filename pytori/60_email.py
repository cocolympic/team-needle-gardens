import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_simple_email():
    smtp_server = "smtp.example.com"
    port = 587
    sender_email = "your_email@example.com"
    password = "your_app_password"
    receiver_email = "recipient@example.com"
    
    message = """
    件名: テストメール
    
    こんにちは！
    
    これはPythonから送信されたテストメールです。
    
    よろしくお願いします。
    """
    
    context = ssl.create_default_context()
    
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.encode('utf-8'))
        print("メールが正常に送信されました")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
