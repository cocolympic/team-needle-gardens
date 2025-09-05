def count_up_to(n):
    print("ジェネレーター開始")
    for i in range(1, n + 1):
        yield i  # 値を1つずつ返す
    print("ジェネレーター終了")

# ジェネレーターを使う
for number in count_up_to(5):
    print(number)