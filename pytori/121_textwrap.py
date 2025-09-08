import textwrap

text = "Python is a powerful programming language."

# 幅10で折り返す
wrapped = textwrap.fill(text, width=10)
print(wrapped)