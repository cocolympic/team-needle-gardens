word = input("数字を入力してください: ")

if word.isdigit():
    number = int(word)
    print(f"入力された数字は {number} です")
else:
    number = None
    print("データがありません")