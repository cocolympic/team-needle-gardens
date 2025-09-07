import re

text = "鮫"
result = re.match(r"鮫", text)

if result:
    print(result.group())