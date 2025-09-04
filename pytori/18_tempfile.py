import tempfile

def main():
    # 一時ファイルを作成
    with tempfile.TemporaryFile(mode="w+t") as tmp:
        tmp.write("tempfile テスト\n")
        tmp.write("一時的に保存\n")
        tmp.seek(0)  # 読み出しのため先頭へ
        print(tmp.read())

if __name__ == "__main__":
    main()