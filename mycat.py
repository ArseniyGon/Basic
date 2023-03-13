class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age=age


barsik=Cat("Barsik", 10)
barsik.set_name("Bars")
print(barsik.get_name())
barsik.age=5
print(barsik.age)

class Dog:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


roy = Dog("Roy", 3)
roy.name = "Rowdy"
print(roy.name)

class People:
    def __init__(self,name,age,occupation):
        self.__name = name
        self.__age = age
        self.__occupation = occupation

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def occupation(self):
        return self.__occupation

    @name.setter
    def name(self, name):
        self.__name = name
    @age.setter
    def age(self, age):
        self.__age = age
    @occupation.setter
    def occupation(self, occupation):
        self.__occupation = occupation

    def show_info(self):
        print(f"Name: {self.__name} Age: {self.__age} Occupation: {self.__occupation}")


jose = People("Jose", 28, "Dishwasher")
brian = People("Brain", 31, "Driver")
joe = People("Joe", 45, "Driver")

joe.show_info()
joe.name = "Joseph"
joe.occupation = "Manager"
joe.show_info()

class American(People):
    def __init__(self, name,age,occupation, company):
        super().__init__(name,age,occupation)
        self.__company = company

    def work(self):
       print("hello")
    def show_info(self):
        super().show_info()
        print(f"Company: {self.__company}")
john = American("John", 50, "Waiter", "McD's")
print(john.name)

john.show_info()
print("_")
def act(people):
    if isinstance(people,American):
        people.work()
    elif isinstance(people,People):
        people.show_info()
act(john)
act(joe)

class 
