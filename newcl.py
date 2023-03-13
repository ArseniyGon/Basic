import functools
from functools import reduce
from decimal import Decimal
import random

# class SomeClass:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}."
#
# obj1 = SomeClass("Tom", 37)
# print(obj1)
#
# def func1():
#     print("Hello")
#
# func1()
#
# l = lambda: print("Hello")
# l()
#
#
# def func2(x):
#     print(f"! {x}")
#
# func2("hello func2")
#
# l1 = lambda x:print(f"! {x}")
# l1("hello func2.2")
#
# def func3(x):
#     return x+1
#
# l2=func3(4)
# print(l2)
#
# l3 = lambda x: x+1
# l4 = l3(4)
# print(l4)
#
# #---------------------------
#
price_list1 = [2, 3, 4, 5]


def price_increase(x):
    return x * 2


new_prices_f = list(map(price_increase, price_list1))
print(new_prices_f)

new_prices_l = list(map(lambda x: x * 2, price_list1))
print(new_prices_l)

new_prices_l_total = reduce(lambda x, y: x + y, new_prices_f)
print(new_prices_l_total)


def total_p(a, b):
    return a + b


new_prices_f_total = reduce(total_p, new_prices_f)
print(new_prices_f_total)

old_price_total = reduce(total_p, price_list1)
print(old_price_total)

cheap = list(filter(lambda x: x < 5, price_list1))
print(cheap)


def not_cheap(x):
    if x > 2:
        return True
    else:
        return False


n_cheap = list(filter(not_cheap, new_prices_f))
print(n_cheap)


def e_func():
    print("x")


e_func()


def x_func(x):
    return x / 2


y = x_func(8)
print(y)
print(int(y))


def a_func(c, d):
    return f"Your answer is: {c + d}."


b = a_func(4, 9)
print(b)

n_l = [1, 6, 2, 9, 3, 7, 4, 5, 9]

print(functools.reduce(lambda a, b: a if a > b else b, n_l))


def fab(a, b):
    if a > b:
        return a
    else:
        return b


print(functools.reduce(fab, n_l))

#
# with open("trial.txt", "r") as hello_file:
#     for line in hello_file:
#         print(line, end="")
#
# with open("trial.txt", "r") as file:
#     contents = file.readlines()
    # str1 = contents[0]
    # str2 = contents[1]
    # print(str1, end="")
    # print(str2)
    # for c in contents:
    #     print(c)

# FILENAME = "trial.txt"
# # определяем пустой список
# messages = list()
#
# for i in range(4):
#     message = input("Введите строку " + str(i + 1) + ": ")
#     messages.append(message + "\n")
#
# # запись списка в файл
# with open(FILENAME, "a") as file:
#     for message in messages:
#         file.write(message)
#
# # считываем сообщения из файла
# print("Считанные сообщения")
# with open(FILENAME, "r") as file:
#     for message in file:
#         print(message, end="")

def func():
    print("")

def func1(x,y):
    return x+y

def func2(x):
    print("")

