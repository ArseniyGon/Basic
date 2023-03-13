class Employees:
    num_of_employees = 0
    raise_amount = 1.04

    def __new__(cls, *args, **kwargs):
        print(cls)
        print(*args)
        print(kwargs.keys())

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + "." + lname + '@company.com'

        Employees.num_of_employees += 1

    # def employee_info(self):
    #     print(f"Name: {self.fname} {self.lname}, Pay: ${self.pay}, Email: {self.email}")

    def __str__(self):
        return f"Name: {self.fname} {self.lname}, Pay: ${self.pay}, Email: {self.email}"

    def give_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Managers(Employees):
    raise_amount = 1.10

    def __init__(self, fname, lname, pay, skill):
        super().__init__(fname, lname, pay)
        self.skill = skill

    def __str__(self):
        return f"Name: {self.fname} {self.lname}, Pay: ${self.pay}, Email: {self.email} Skill: {self.skill}"

    def __del__(self):
        print('удаляется объект {} класса SomeClass'.format(self.fname))

    def __call__(self, x, y):
        return x * y


class Subordinates(Employees):
    pass


mgr_1 = Managers("Tim", "Spivak", 8500, "Python")
mgr_2 = Managers("John", "Thompson", 8200, "Java")
emp_1 = Subordinates("Corey", "Schafer", 5000)
emp_2 = Subordinates("Bob", "Johnson", 6500)
emp_3 = Subordinates("Alex", "Doe", 5750)
emp_4 = Subordinates("Nicole", "Smith", 6700)

print(emp_1)
print(mgr_1)
print(Employees.num_of_employees)
print(mgr_1.pay)
mgr_1.give_raise()
print(mgr_1.pay)
print(mgr_1.lname)
emp_2.give_raise()
print(emp_2.pay)
print(emp_2)
mgr_1(5, 4)

class Example:
    def __init__(self):
        print("Instance Created")

    # Defining __call__ method
    def __call__(self, x, y):
        print("Instance is called via special method")
        return x+y


# Instance created
e = Example()

# __call__ method will be called
print(e(3, 5))


# class Person:
#     def __init__(self):
#         self.name = 'Manjula'
#         self.__lastname = 'Dube'
#
#     def PrintName(self):
#         return self.name + ' ' + self.__lastname
#
#
# # Outside class
# P = Person()
# print(P.name)
# print(P.PrintName())
# print(P.__lastname)
#
#
# class SeeMee:
#     def youcanseeme(self):
#         return 'you can see me'
#
#     def __youcannotseeme(self):
#         return 'you cannot see me'
#
#
# # Outside class
# Check = SeeMee()
# print(Check.youcanseeme())
# # you can see me
# print(Check.__youcannotseeme())
# # AttributeError: 'SeeMee' object has no attribute '__youcannotseeme'
