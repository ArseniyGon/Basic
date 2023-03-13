class Car:

    def __init__(self, model, speed):
        self.__model = model
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if 1 < speed < 120:
            self.__speed = speed
        else:
            print("Speed limit has been reached at 120/mph")

    @property
    def model(self):
        return self.__model

    def __str__(self):
        return f"{self.model}, {self.speed}"

    def info(self):
        print(f"{self.model}, {self.speed}")

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Car):
            return self.speed == other.speed and self.model == other.model
        return False

    def __hash__(self):

        # hash(custom_object)
        return hash((self.model, self.speed))

    @staticmethod
    def static_func():
        print("Static Method")
Car.static_func()

car = Car("Mercedes", 120)
car.static_func()
print(car)
car.info()
print(car.model)
car.speed = -10
print(car.speed)
car.speed = 130
print(car.speed)


class Brand(Car):

    def cheaper(self):
        super().info()
        print(f"{self.model} is cheaper.")

    def info(self):
        super().info()
        # print("!")
honda = Brand("Honda", 80)

print(honda)
honda.info()
honda.cheaper()

class Expensive(Brand):

    def cheaper(self):
        print(f"{self.model} is not cheaper")

bentley = Expensive("Bentley", 180)

bentley.cheaper()

people = ["Tom", "Bob", "Sam"]

tom, bob, sam = people
# tom = people[0]
# bob = people[1]
# sam = people[2]

car1 = Car("Mercedes", 100)
car2 = Car("Ford", 100)
car3 = Car("BMW", 120)
print(car1==car2)
cars = [car1, car2, car3]
cars_tuple = (car1,car2,car3)
cars_dict = {"car1k": car1, "car2k": car2, "car3k": car3}
cars_dict["car4k"] = car1

cars_set = {car1, car2, car3, car1}
for i in cars_set:
    print(i)
print(len(cars_set))
car4 = Car("Toyota", 75)
cars_set.add(car4)
for i in cars_set:
    print(i)
print(car4 in cars_set)
print("-")
cars_set.remove(car4)
for k in cars_set:
    print(k)
print("-")
cars_set2 = cars_set.copy()
cars_set2.discard(car1)
for i in cars_set2:
    print(i)
print("-")

cars_set3 = cars_set2.union(cars_set)
for i in cars_set3:
    print(i)


# for i in cars_dict:
#     print(f"{i} {cars_dict[i]}")
# for k, value in cars_dict.items():
#     print(f"{k} {value}")
#
# for i in cars_tuple:
#     print(i.speed)
# # cars.append(Car("Ferrari", 200))
# #
# # cars.insert(0, Car("Honda", 85))
# #
# # cars.pop(1)
# for i in cars:
#     print(i)
# print("_")
# # print(cars.pop())
# # cars.remove(car1)
#
# print("_")
# for i in cars:
#     print(i)
# print(cars.count(car1))
# print(len(cars))
# # del cars[1]
# del cars[1:]
# for i in cars:
#     print(i)
#
str = "Abb"
# str[0] = "c"
print(str[0])
