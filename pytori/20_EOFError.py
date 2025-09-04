import logging

def main():
    try:
        # 意図的に EOFError を発生させる
        raise EOFError("これは意図的な EOFError です")
    except EOFError as e:
        logging.error("EOFError が発生しました", exc_info=e)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()