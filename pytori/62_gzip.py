import gzip

text = "レイチェル・ガードナー"

# テキストをgzip圧縮して保存
with gzip.open("example.txt.gz", "wt", encoding="utf-8") as f:
    f.write(text)