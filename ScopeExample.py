n = 10


def outer():  # внешняя функция
    n = 5

    def inner():  # вложенная функция
        global n
        # nonlocal n
        n = 25
        print(n)

    #
    inner()
    print(n)


outer()

a = "Hello World"
print(a.replace("H", "J"))

a = "Hello, World"
print(a.split("o"))

a = "  Hello, World!     "
print(a)
print(a.strip())


# order of variables used:
# L = local variables
# E = enclosing variables
# G = global
# B = built in

def myfunc():
    x = 300
    print("!")

    def myinnerfunc():
        print(x)
    # myinnerfunc()


myfunc()


def print_hello(language):
    match language:
        case "russian":
            print("Привет")
        case "english":
            print("Hello")
        case "german":
            print("Hallo")
        case _:
            print("Not available")


print_hello("italian")


def operation(a, b, code):
    match code:
        case 1:
            return a + b
        case 2:
            return a - b
        case 3:
            return a * b
        case _:
            return 0


x1 = operation(1, 2, 1)
x2 = operation(3, 3, 3)
print(operation(1, 2, 4))
print(x1)
print(x2)

people = ["Tom", "Sam", "Bob"]
for person in people:
    print(person)

people = [
    ["Tom", 29],
    ["Alice", 33],
    ["Bob", 27]
]

print(people[0])  # ["Tom", 29]
print(people[0][0])  # Tom
print(people[0][1])  # 29


# people = [
#     ["Tom", 29],
#     ["Alice", 33],
#     ["Bob", 27]
# ]
#
# for person in people:
#     for item in person:
#         print(item, end=" | ")


def get_user():
    name = "Tom"
    age = 22
    company = "Google"
    return name, age, company


user = get_user()
print(user)


def cat():
    name = "Barsik"
    size = "medium"
    age = 7
    return name, size, age


c = cat()
print(c[0])


def print_person(name, age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")


person1 = ("Tom", 34, "Google")
for item in person1:
    print(item)

tom = ("Tom", 22, "Google")
print(len(tom))
i = 0
while i < len(tom):
    print(tom[i])
    i += 1

s = "lorem"
s = s.index("l")
print(s)

print("\n")

nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print("Found!")
        break
    print(num)

a = [1, 2, 3, 4, 5]

for num in a:
    if num == 3:
        print("Found!")
        continue
    print(a)


def client_list(client):
    match client:
        case "Tom":
            print("Econom Tom")
        case "Alice":
            print("Standard")
        case "Bob":
            print("Premium")


client_list("Tom")


def client_list1(client):
    match client:
        case ["Tom", "Bob"]:
            print("Econom Tom")
        case ["Alice", _]:
            print("Standard")
        case ["Bob", "Alice", "Tom"]:
            print("Premium")
        case ["Ed", *_]:
            print("Ed")
            # for o in other:
            #     print(o)


client_list1(["Ed", "Alice", "Tom", "Bob"])


def client_list2(client):
    match client:
        case ("Tom", "Bob"):
            print("Economy Tom")
        case ("Alice", _):
            print("Standard")
        case ("Bob", "Alice", "Tom"):
            print("Premium")
        case ("Ed" | "Edward", *other):
            print("Ed")
            for o in other:
                print(o)


client_list2(("Edward", "1"))

for i in range(1, 10, ):
    for j in range(1, 10, ):
        print(i * j, end="\t")
    print("\n")

person = {"name": "John Doe", "age": 25, "phone": "555-5555", "address": "123 Random Street, Brooklyn, New York."}
print(person["name"])
print(person.get("age"))
print(person.keys())
print(person.values())
person["age"] = 37
print(person["age"])
person.update({"name": "Mark Johnson"})
print(person["name"])
for x in person.keys():
    print(x)
for y in person.values():
    print(y)
for x, y in person.items():
    print(x, y)
age = person.pop("age")
print(person)
print(age)
print(age)
print(len(person))
person.update({"age": 37})
print(person)
person["income"] = "$50,000"
print(person)
print(person.keys())
del person["income"]
print(person)


def cat(cats):
    match cats:
        case {"name": "barsik" | "bars", "age": 1}:
            print("home cat")
        case {"name": "mursik", "age": 3}:
            print("street cat")
        case {"name": "guy", "age": "6mos"}:
            print("kitten")


cat({"name": "bars", "age": 1})


def look(words):
    match words:
        case {"red": red, **rest}:
            print(f"red: {red}")
            for key in rest:  # rest - тоже словарь
                print(f"{key}: {rest[key]}")


look({"red": "красный", "blue": "синий", "green": "зеленый"})


def outer():
    n = 3

    def inner():
        nonlocal n
        n += 1
        print(n)

    return inner


x = outer()
x()
x()
x()


def multiply(n):
    def inner(m):
        print(n * m)
        return n * m

    return inner


fn = multiply(5)
fn(5)


# hm

def select(input_func):
    def output_func():  # определяем функцию, которая будет выполняться вместо оригинальной
        print("*****************")  # перед выводом оригинальной функции выводим всякую звездочки
        input_func()  # вызов оригинальной функции
        print("*****************")  # после вывода оригинальной функции выводим всякую звездочки

    return output_func  # возвращаем новую функцию


def mydecor(input_func):
    def output_func():
        print("!!!!")
        input_func()
        print("!!!!")

    return output_func


# определение оригинальной функции
@select  # применение декоратора select
def hello():
    print("Hello METANIT.COM")


# вызов оригинальной функции
hello()


@mydecor
def multiply1():
    print("multiply")


multiply1()


# определение функции декоратора
def check(input_func):
    def output_func(*args):  # через *args получаем значения параметров оригинальной функции
        print("???")
        input_func(*args)  # вызов оригинальной функции
        print("???")

    return output_func  # возвращаем новую функцию


# определение оригинальной функции
@check
def print_person(name, age):
    print(f"Name: {name}  Age: {age}")


@check
def square(i):
    print(i * i)


# вызов оригинальной функции
print_person("Tom", 38)

square(5)


def check(input_func):
    def output_func(*args):
        name = args[0]
        age = args[1]  # получаем значение второго параметра
        if age < 0: age = 1  # если возраст отрицательный, изменяем его значение на 1
        input_func(name, age)  # передаем функции значения для параметров

    return output_func


# определение оригинальной функции
@check
def print_person(name, age):
    print(f"Name: {name}  Age: {age}")


# вызов оригинальной функции
print_person("Tom", 38)
print_person("Bob", -5)


def check(input_func):
    def output_func(*args):
        result = input_func(*args)  # передаем функции значения для параметров
        if result < 0: result = 0  # если результат функции меньше нуля, то возвращаем 0
        return result

    return output_func


# определение оригинальной функции
@check
def sum(a, b):
    return a + b


# вызов оригинальной функции
result1 = sum(10, 20)
print(result1)  # 30

result2 = sum(10, -20)
print(result2)


def say_hello(): print("Hello")


def say_bye(): print("Bye")


message = say_hello
message()
message = say_bye
message()


def sum01(a, b): return a + b


def multiply01(a, b): return a * b


operation = sum01
result = (operation(5, 6))
print(result)

operation = multiply01
result = (operation(5, 6))
print(result)


def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")
def sum(a, b): return a + b
def multiply(h, k): return h * k

def get_even(numbers):
    even_numbers=[]
    for n in numbers:
        if n % 2==0:
            even_numbers.append(n)
    # even_numbers = [num for n in numbers if n%2]
    return even_numbers
    print("!")


print(get_even([1,2,3,4,5,6,7,8]))


