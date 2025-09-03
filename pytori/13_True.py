#無限に入力する処理(eで終了)
words = []  

while True:
    word = input("何か入力してください (eで終了): ")
    if word == "e":
        print("\n終了します\n")
        break
    else:
        words.append(word)

print("=== 入力履歴 ===")
for i, w in enumerate(words, start=1):
    print(f"{i} 回目: {w}")