from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, size, weight):
        self.size = size
        self.weight = weight


    def __str__(self):
        return str(self.size) + " " + str(self.weight)

obj1 = Animal(1, 3)
class Cat(Animal):
    def __init__(self, size, weight, rank=0):
        super().__init__(size, weight)
        self.rank = rank




class Dog(Animal):
    def __init__(self, size, weight, rank = 0):
        super().__init__(size, weight)
        self.rank = rank

dog1 = Dog(1, 10)
dog2 = Dog(2, 15)
dog3 = Dog(3, 20)
cat1 = Cat(1, 5)
cat2 = Cat(2, 5)
cat3 = Cat(3, 5)


animals = []
animals.append(cat1)
animals.append(cat2)
animals.append(cat3)
animals.append(dog1)
animals.append(dog2)
animals.append(dog3)
animals.sort(key=lambda a: a.weight)
rank = 0
for x in animals:
    rank = rank+1
    x.rank = rank
    # print(x.weight)
    # print(x.rank)
cats = []
dogs = []
for y in animals:
    if isinstance(y, Cat):
        cats.append(y)
    elif isinstance(y, Dog):
        dogs.append(y)

cats_rank = 0
dogs_rank = 0
for i in animals:
    if isinstance(i, Cat):
        cats_rank = cats_rank+i.rank
    elif isinstance(i, Dog):
        dogs_rank = dogs_rank+i.rank

print(str(cats_rank)+ " " + str(dogs_rank))
for x in animals:
    print(x.rank)