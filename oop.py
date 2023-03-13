# class Salary:
#     def __init__(self,pay):
#         self.pay = pay
#
#     def getTotal(self):
#         return (self.pay*12)
#
# class Employee:
#     def __init__(self,pay,bonus):
#         self.pay = pay
#         self.bonus = bonus
#         self.salary = Salary(self.pay)
#
#     def annualSalary(self):
#         return "Total: " + str(self.salary.getTotal() + self.bonus)
#
# employee = Employee(100,10)
# print(employee.annualSalary())

# class Salary(object):
#     def __init__(self, pay):
#         self.pay = pay
#
#     def getTotal(self):
#         return (self.pay * 12)
#
# class Employee(object):
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus
#
#     def annualSalary(self):
#         return "Total: " + str(self.pay.getTotal() + self.bonus)
#
# salary = Salary(100)
# employee = Employee(salary, 10)
# print(employee.annualSalary())

# try:
#     number = int(input("Введите число: "))
#     print("Введенное число:", number)
# except:
#     print("Преобразование прошло неудачно")
#     print("Завершение программы")
#
# try:
#     number = int(input("Введите число: "))
#     print("Введенное число:", number)
# except:
#     print("Преобразование прошло неудачно")
# finally:
#     print("Блок try завершил выполнение")
# print("Завершение программы")

# try:
#     number1 = int(input("Введите первое число: "))
#     number2 = int(input("Введите второе число: "))
#     print("Результат деления:", number1/number2)
# except ValueError as v:
#     print("Преобразование прошло неудачно" + v)
# except ZeroDivisionError as z:
#     print("Попытка деления числа на ноль")
# except BaseException:
#     print("Общее исключение")
# print("Завершение программы")
#
# try:
#     number1 = int(input("Введите первое число: "))
#     number2 = int(input("Введите второе число: "))
#     if number2 == 2:
#         raise Exception("Второе число не должно быть равно 0")
#     print("Результат деления двух чисел:", number1/number2)
# except ValueError:
#     print("Введены некорректные данные")
# except Exception as e:
#     print(e)
# print("Завершение программы")




class PersonAgeException(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return f"Недопустимое значение: {self.age}. " \
               f"Возраст должен быть в диапазоне от {self.minage} до {self.maxage}"


class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        minage, maxage = 1, 110
        if minage < age < maxage:  # устанавливаем возраст, если передано корректное значение
            self.__age = age
        else:  # иначе генерируем исключение
            raise PersonAgeException(age, minage, maxage)

    def display_info(self):
        print(f"Имя: {self.__name}  Возраст: {self.__age}")


try:
    tom = Person("Tom", 37)
    tom.display_info()  # Имя: Tom  Возраст: 37

    bob = Person("Bob", -23)
    bob.display_info()
except PersonAgeException as e:
    print(e)