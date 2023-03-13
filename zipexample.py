from functools import reduce

# groceries = ["apples", "banas", "carrots", "potatoes", "milk"]
# new_list = []
# # for i in groceries:
# #     new_list.append(i + "!")
# # print(new_list)
#
# new_list = list(map(lambda x:x+"!", groceries))
# print(new_list)
#
# new_list1 = list(filter(lambda x:len(x)>5,groceries))
# print(new_list1)
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result_sum = reduce(lambda x, y: x + y, numbers)
print(result_sum)


def multiply(a, b):
    return a * b


fact = [5, 4, 3, 2, 1]
result_mul = reduce(multiply, fact)
print(result_mul)

fact1 = [6, 5, 4, 3, 2, 1]
result_fact1 = reduce(lambda x, y: x * y, fact1)
print(result_fact1)

people = ["john", "bob", "kat", "don"]
new_people = list(map(lambda p: p + " doe", people))
print(new_people)

items = [1, 2, 3, 4, 5]
new_items = []
for x in items:
    new_items.append(x + 1)
print(new_items)

new_items1 = list(map(lambda x: x + 1, items))
print(new_items1)


def plus_one(a):
    return a + 1


new_items2 = list(map(plus_one, items))
print(new_items2)

new_items3 = list(filter(lambda x: x > 3, items))
print(new_items3)


def pfunc(x):
    if x < 3:
        return True
    else:
        return False


new_items4 = list(filter(pfunc, items))
print(new_items4)

list5 = [1, 2, 3, 4, 5, 6, 7]
list6 = []
for x in list5:
    list6.append(x + 1)
print(list6)

list7 = list(map(lambda x: x + 1, list5))
print(list7)

list8 = list(filter(lambda x: x < 5, list5))
print(list8)

y = 0
for x in list5:
    y = x + y
print(y)

list9 = reduce(lambda x, y: x + y, list5)
print(list9)

