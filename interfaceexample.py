from abc import ABCMeta, abstractmethod, abstractproperty


class Movable():
    __metaclass__ = ABCMeta

    @abstractmethod
    def move(self):
        """Переместить объект"""

    @abstractproperty
    def speed(self):
        """Скорость объекта"""

class Car(Movable):
    def __init__(self):
        self.speed = 10
        self.x = 0

    def move(self):
        return 100

class Ship(Movable):
    def move(self):
        print("Floating")

    @property
    def speed(self):
        return 10

ship1 = Ship()
ship1.move()

class Plane(Movable):
    def __init__(self, speed):
        self.__speed = speed


    def move(self):
        print('Flying' + str(self.__speed))

    @property
    def speed(self):
        return self.__speed

plane1 = Plane(1000)
plane1.move()
