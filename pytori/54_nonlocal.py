def make_counter():
    count = 0
    
    def increment():
        nonlocal count  # 外側の関数のcount変数を参照
        count += 1
        return count
    
    def decrement():
        nonlocal count
        count -= 1
        return count
    
    def get_count():
        return count
    
    return increment, decrement, get_count

# 使用例
inc, dec, get = make_counter()
print(f"初期値: {get()}")  # 0
print(f"インクリメント: {inc()}")  # 1
print(f"インクリメント: {inc()}")  # 2
print(f"デクリメント: {dec()}")  # 1
print(f"現在の値: {get()}")  # 1
