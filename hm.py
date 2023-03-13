def fibonacci(n):
    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(9))


def factorial(h):
    if (h <= 0):
        return 1
    return h * factorial(h - 1)


print(factorial(5))


def chess():
    for y in range(4):
        # if(y % 2==0):
        for x in range(8):
            if x % 2 == 0:
                print("()", end="\t")
            else:
                print("[]", end="\t")
        print("")
        # else:
        for x in range(8):
            if x % 2 != 0:
                print("()", end="\t")
            else:
                print("[]", end="\t")
        print("")


# y=chess
# y()
z = lambda: print("lambda")
v = lambda x: x * x
print(v(4))


def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")


# def sum(a, b):
#     return a + b
#
# print (sum(4,5))
# o=sum
# do_operation(4,5,o)
# do_operation(4,5,lambda x,y:x+y)


# def do_operation(a, b, operation):
#     result = operation(a, b)
#     print(f"result = {result}")
#
#
# def sum(a, b): return a + b
#
#
# def multiply(a, b): return a * b
#
#
# do_operation(5, 4, lambda a,b:a+b)  # result = 9
# do_operation(5, 4, sum)  # result = 9
# do_operation(5, 4, lambda a,b:a*b)


# def sum(a, b): return a + b
#
#
# def subtract(a, b): return a - b
#
#
# def multiply(a, b): return a * b
#
#
# def select_operation(choice):
#     if choice == 1:
#         return lambda a, b: a + b
#         # return sum
#     elif choice == 2:
#         # return subtract
#         return lambda a, b: a - b
#     else:
#         # return multiply
#         return lambda a, b: a * b


# operation = select_operation(1)  # operation = sum
# print(operation(10, 6))  # 16
#
# operation = select_operation(2)  # operation = subtract
# print(operation(10, 6))  # 4
#
# operation = select_operation(3)  # operation = multiply
# print(operation(10, 6))  # 60


def say_hello(): print("Hello")


def say_goodbye(): print("Good Bye")


message = say_hello
message()  # Hello
message = say_goodbye
message()  # Good Bye

# def sum(a, b): return a + b
#
#
# def multiply(a, b): return a * b
#
#
# operation = sum
# result = operation(5, 6)
# print(result)  # 11
#
# operation = multiply
# print(operation(5, 6))
#
#
# def do_operation(a, b, operation):
#     result = operation(a, b)
#     print(f"result = {result}")
#
#
# def sum(a, b): return a + b
#
#
# def multiply(a, b): return a * b
#

# do_operation(5, 4, sum)  # result = 9
# do_operation(5, 4, multiply)  # result = 20
#
#
# def sum(a, b): return a + b
#
#
# def subtract(a, b): return a - b
#
#
# def multiply(a, b): return a * b
#
#
# def select_operation(choice):
#     if choice == 1:
#         return sum
#     elif choice == 2:
#         return subtract
#     else:
#         return multiply
#
#
# operation = select_operation(1)  # operation = sum
# print(operation(10, 6))  # 16
#
# operation = select_operation(2)  # operation = subtract
# print(operation(10, 6))  # 4
#
# operation = select_operation(3)  # operation = multiply
# print(operation(10, 6))  # 60

sum = lambda a, b: a + b
print(sum(4, 10))

subtract = lambda a, b: a - b
print(subtract(10, 7))

multiply = lambda a, b: a * b
print(multiply(3, 3))

def select_operation (n):
    if n ==1:
        return sum
    elif n==2:
        return subtract
    else:
        return multiply

x = select_operation (1)
y=sum
print (y(1,2))

def do_operation(a,b, op):
    print(op(a,b))

do_operation(1,3,lambda a,b:a+b)

a = 2
b = "3"
c = a + int(b)
print (c)

text = ("Laudate \"omnes gentes\" laudate "
        "Magnificat\' in\n secula ")
print(text)

text = '''
Laudate "omnes gentes laudate"
      Magnificat in secula
Et anima mea laudate
Magnificat in secula 
'''
print(text)

'''
Это комментарий 
'''

path = r"C:\python\name.txt"
print(path)

a = "John"
b = "Smith"
print (f"My name is {a} and {b}")
print ("My name is " + a + " and " + b)

# string = "hello world"
# string[1] = "R"
#
# string = "hello world"
# for char in string:
#     print(char)

string = "hello world"

# с 0 до 5 индекса
sub_string1 = string[:5]
print(sub_string1)  # hello

# со 2 до 5 индекса
sub_string2 = string[2:5]
print(sub_string2)  # llo

# с 2 по 9 индекса через один символ
sub_string3 = string[2:9:2]
print(sub_string3)  # lowr

name = "Tom"
surname = "Smith"
age = str(35)
s =f"{name} {surname} {35} \n"
print(s * 2)

str1 = "1"
str2 = "a"
str3 = "A"

print(str2 > str3)

print(ord("a"))

s= "hello world"
m = "hello" in s
print(m)  # True

exist = "sword" in s
print(exist)  # False

# string = input("Введите число: ")
# if string.isnumeric():
#     number = int(string)
#     print(number)

words = ["Let", "me", "speak", "from", "my", "heart", "in", "English"]
# разделитель - пробел
sentence = " ".join(words)
print(sentence)

my_array = sentence.split(" ")
print(my_array[0])
my_name="John"
print(f"Hello {my_name}")
text = "Hello, {first_name}.".format(first_name=my_name)
print(text)  # Hello, Tom.

info = "Name: {name}\t Age: {age}".format(name="Bob", age="Bob")
info = "Name: {0}\t Age: {1}".format(23, 23)
print(info)  # Name: Bob  Age: 23

welcome = "Hello {:d}"
name = "Tom"
formatted_welcome = welcome.format(1)
formatted_welcome = "Hello {:d}".format(1)
print(formatted_welcome)

print("{:8.4f}".format(1.8589578))    #     23.86
print("{:8d}".format(25))               #      25

info = "Имя: %s \t Возраст: %d" % ("Tom", 35)
print(info)   # Имя: Tom     Возраст: 35


def fibonacci(h):
    if h in {0, 1}:
        return 1
    return fibonacci(h - 1) + fibonacci(h - 2)

print(fibonacci(3))

def factorial(a):
    if a<=0:
        return 1
    return a * factorial(a-1)
print(factorial(5))

def sum(x, y):
    return x+y
print(sum(4,5))






def dec(input_func):
    def output_func():
        print("-==-")
        input_func()
        print("-==-")

    return output_func


@dec
def sum():
    print("sum")


sum()