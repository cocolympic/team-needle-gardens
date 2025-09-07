from enum import Enum, auto

class Animal(Enum):
    DOG = auto()
    CAT = auto()
    BIRD = auto()

print(list(Animal))