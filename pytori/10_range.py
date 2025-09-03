#range()を用いたクイズ(問題は某ゲームから引用)
tuple_qes = ("イセエビ","ウナギ","サメ","→sea","スズキ","フグ","イカ","ウナギ","→blue")
tuple_qes2 = ("アユ","イカ","サザエ","サメ","→?")

print("【問題1】")
for i in range(4):
    print(f"{i+1}. {tuple_qes[i]}")
print()

print("【問題2】")
for i in range(4, 9):
    print(f"{i-3}. {tuple_qes[i]}")
print()

print("【問題3】")
for i in range(5):
    print(f"{i+1}. {tuple_qes2[i]}")