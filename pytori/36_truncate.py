from io import StringIO

def basic_truncate_example():
    # StringIOオブジェクトを作成してデータを書き込む
    sio = StringIO()
    sio.write("Hello, World! This is a long string.")
    print(f"元の内容: '{sio.getvalue()}'")
    print(f"元の長さ: {len(sio.getvalue())}")
    # 位置10で切り詰める
    sio.truncate(10)
    print(f"truncate(10)後: '{sio.getvalue()}'")
    print(f"新しい長さ: {len(sio.getvalue())}")
    print()
