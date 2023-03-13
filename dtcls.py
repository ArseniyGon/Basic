from dataclasses import dataclass, field
import copy



# @dataclass
# class StoreItems:
#     item_name: str
#     item_price: float
#     item_quantity: int
#
#     def __str__(self):
#         return f"Item: {self.item_name} Price: {self.item_price} In Stock: {self.item_quantity}"
#
#
# pen = StoreItems("Bic Pen.", .99, 100)
# notebook = StoreItems("Basic Notebook.", 1.25, 75)
# bag = StoreItems("Sport Book Bag.", 35.00, 20)
# print(pen)
# print(notebook)
# print(bag)

# print(hex(10))
# @dataclass
# class Person:
#      first_name: str = "Ahmed"
#      last_name: str = "Besbes"
#      age: int = 30
#      job: str = "Data Scientist"
#      full_name: str = field(init=False, repr=False)
#      def __post_init__(self):
#          self.full_name = self.first_name + " " + self.last_name
#
# ahmed = Person()
# rajesh = Person()
# x = "Hello"
# y = "Hello"

# print(id(x))
# x = "bye"
# print(id(x))
#
# l1 = [1,2,3,4,5]
# print(id(l1))
# l1.append(10)
# print(id(l1))
# print(l1)

# test_1 = [1, 2, 3, [1, 2, 3]]
# test_copy = copy.copy(test_1)
#
# test_1.append(10)
# print(test_copy, "-", test_1)


# print(ahmed)
# print(id(x))
# print(id(y))
#
# print(x is y)
#
# print(ahmed is rajesh)
# print(type(ahmed))
# print(type(x))

# print(id(ahmed))
# print(id(rajesh))
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"Person(name={self.name!r}, age={self.age!r}"
#
#     def __eq__(self, other):
#         if other.__class__ is self.__class__:
#             return (self.name) == (other.name)
#         return NotImplemented
#
# obj1 = Person("Tom", 20)
# obj2 = Person("Tom", 30)
# print(obj1 == obj2)
#
# print(obj1)
# print(obj2)


sublist = []
outer_list = [42, 73, sublist]
copy_list = copy.copy(outer_list)
sublist.append(73)
print(outer_list, "-", copy_list)
