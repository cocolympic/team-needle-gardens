try:
    x = int(input("数字を入力してください: "))  
    print("入力された数字は:", x)
except ValueError:
    print("エラー: 数字を入力してください！")