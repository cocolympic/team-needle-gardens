class MyClass:
    x = 10
    y = 20

obj = MyClass()
print(obj.x, obj.y)  # 10 20

delattr(obj, "x")    # x を削除

print(hasattr(obj, "x"))  # False
print(obj.y) 