import ast

s = "[1, 2, 3]"
data = ast.literal_eval(s)  # 安全に評価できる
print(data)