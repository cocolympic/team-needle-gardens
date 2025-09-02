def main():
    fruits = ["カレー", "ハヤシライス", "牛丼", "クッパ"]

    print("=== 今日の夜ご飯 ===")
    for i, fruit in enumerate(fruits, start=1):
        print(f"{i}. {fruit}")

if __name__ == "__main__":
    main()