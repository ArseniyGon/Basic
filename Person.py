class Person:
    default_name = "Undefined"
    def __init__(self, name, age=10):
        self.__name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


    def __str__(self):
        return self.name + str(self.age)

person1 = Person("Tom")

print(person1)

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name, 10)
        self.salary = salary

    def __str__(self):
        return super().__str__() + " " + str(self.salary)

    @staticmethod
    def fn1():
        print("Hello")

person2 = Employee("Bob", 500)

print(person2)

print(Person.default_name)
Employee.fn1()
print(person2.default_name)
person2.fn1()


