import traceback

try:
    x = [1, 2, 3]
    print(x[5])
except Exception:
    error_msg = traceback.format_exc()
    print("エラー内容:")
    print(error_msg)