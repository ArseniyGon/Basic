# class Person:
#     # конструктор
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         print("Создание объекта Person")
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     def say_hello(self, message):
#         print(f"Hello {message}")
#
#
# tom = Person("Tom", 5)
# tom.name = "Tom Black"
# print(tom.name)
# bob = Person("Bob", 10)
# tom.say_hello("Tom")
#
#
# class Cat:
#
#     def __init__(self, name, breed, age):
#         self.__name = name
#         self.__breed = breed
#         self.__age = age
#
#     def set_breed(self, breed):
#         self.__breed = breed
#
#     def get_breed(self):
#         return self.__breed
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     def cat_info(self):
#         print(f"Name: {self.__name}  Breed: {self.__breed}  Age: {self.__age}")
#
#
# barsik = Cat("Barsik", "Stray", "Kitten")
#
# barsik.set_breed("Seam")
# print(barsik.get_breed())
# barsik.name = "New Name"
# print(barsik.name)
# barsik.cat_info()


class Products:
    def __init__(self, item, price):
        self.__item = item
        self.__price = price

    def get_price(self):
        return self.__price+10

    def set_price(self, price):
        self.__price=price+1

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, item):
        self.__item=item

    def items(self):
        print(f"Item: {self.__item}  Price: {self.__price}")


item1 = Products("Paper", 5)
item2 = Products("Pens", 3)
item3 = Products("Folder", 2)
item1.set_price(4)
item1.item="marker"
print(item1.get_price())
print(item1.item)

item1.items()