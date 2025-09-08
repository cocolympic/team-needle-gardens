from collections import namedtuple

# namedtupleを定義（Personという名前の型を作成）
Person = namedtuple("Person", ["name", "age", "city"])

# インスタンスを作成
p1 = Person(name="Alice", age=30, city="Tokyo")
p2 = Person(name="Bob", age=25, city="Osaka")

# フィールド名でアクセス
print(p1.name)   # Alice
print(p1.age)    # 30
print(p1.city)   # Tokyo
