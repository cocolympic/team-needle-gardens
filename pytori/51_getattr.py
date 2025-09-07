class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"こんにちは、私は{self.name}です"

person = Person("田中", 25)

# 通常の属性アクセス
print(person.name)  # 田中

# getattrを使った属性アクセス
name = getattr(person, 'name')
print(name)  # 田中
