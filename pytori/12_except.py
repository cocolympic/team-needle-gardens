try:
    number = int(input("数字を入力してください: "))
    result = 10 / number
    print(f"10 ÷ {number} = {result}")
except ValueError:
    print("エラー: 数字以外が入力されました")
except ZeroDivisionError:
    print("エラー: ゼロで割ることはできません")
except Exception as e:
    print(f"予期しないエラーが発生しました: {e}")
