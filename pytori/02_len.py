#長さによって表示内容が変わるプログラム
def text_judge(text: str) -> str:
    length = len(text)
    if length == 0:
        return "…何も書かれてないよ？"
    elif length < 10:
        return "この短さは... まるで川柳の如く..."
    elif length < 30:
        return "これほど心地よくまとめてみせるとは... お主何者だ..."
    else:
        return "これはこれは... これから始まるあなたの物語の序章を感じさせますな..."

def main():
    text = input("好きに文字を入力してください... あなたの文章力を試します...\n>>> ")
    print("\n--- 分析結果 ---")
    print(f"文字数: {len(text)}")
    print(f"単語数: {len(text.split())}")
    print("コメント:", text_judge(text))

if __name__ == "__main__":
    main()