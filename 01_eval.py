result1 = eval("4 * 60")
result2 = eval("4 * 60", {"__builtins__": None}, {})
print(result1)
print(result2)