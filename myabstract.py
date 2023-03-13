from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def voice(self):
        pass
    @abstractmethod
    def move(self):
        print("Move")

class Dog(Animal):
    dog_name = "Dog"
    def __init__(self):
        self.name = Dog.dog_name
    @staticmethod
    def say_hello():
        print("Hello")
    def voice(self):
        print("Woof")

    def move(self):
        super().move()
        print("Dog Running")



class Cat(Animal):
    def voice(self):
        print("Meow")

    @abstractmethod
    def move(self):
        super().move()
        print("Cat Running")
rowdy = Dog()
rowdy.voice()
rowdy.move()
print(rowdy.name)
Dog.say_hello()