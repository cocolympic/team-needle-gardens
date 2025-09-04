def validate_positive(value):
    if value < 0:
        raise Exception("0以上の値を入力してください")
    return value

try:
    num = validate_positive(int(input("数値を入力してください: ")))
    print(f"入力された値は {num} です。")
except Exception as e:
    print(f"エラーが発生しました: {e}")