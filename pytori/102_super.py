class Animal:
    def speak(self):
        print("Test Txst")

class Dog(Animal):
    def speak(self):
        super().speak() 
        print("Test")

dog = Dog()
dog.speak()