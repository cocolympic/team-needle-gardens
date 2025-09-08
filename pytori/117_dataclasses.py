from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str = "unknown@example.com"  # デフォルト値を設定可能

# インスタンス生成
p1 = Person(name="Alice", age=30)
p2 = Person(name="Bob", age=25, email="bob@example.com")

# 自動で __repr__ が生成される
print(p1)  # Person(name='Alice', age=30, email='unknown@example.com')
print(p2)  # Person(name='Bob', age=25, email='bob@example.com')

# __eq__ も自動で生成される
print(p1 == p2)  # False

# フィールドにアクセス
print(p1.name)  # Alice
print(p2.email) # bob@example.com
