user_data = {
    "name": "田中太郎",
    "age": 30,
    "city": "東京"
}

try:
    # 存在しないキーにアクセス
    email = user_data["email"]  # KeyErrorが発生
    print(f"メールアドレス: {email}")
except KeyError as e:
    print(f"KeyError: キー {e} が見つかりません")
