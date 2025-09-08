import threading
import time

# スレッドで実行する関数
def worker(name, delay):
    for i in range(3):
        print(f"スレッド {name}: {i}")
        time.sleep(delay)
    print(f"スレッド {name} 完了")

# メイン処理
if __name__ == "__main__":
    # スレッドを作成
    t1 = threading.Thread(target=worker, args=("A", 1))
    t2 = threading.Thread(target=worker, args=("B", 2))

    # スレッドを開始
    t1.start()
    t2.start()

    # スレッドの終了を待つ
    t1.join()
    t2.join()

    print("全てのスレッドが終了しました")
