import traceback

def divide(a, b):
    return a / b

try:
    result = divide(10, 0)  # 0で割るのでエラーを出させる
except Exception as e:
    print("エラーが発生しました!")
    # トレースバックを文字列として出力
    tb_str = traceback.format_exc()
    print(tb_str)