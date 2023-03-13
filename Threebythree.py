class Races:
    def __init__(self, sex, start_level, start_health):
        self.sex = sex #male | female
        self.__start_level = start_level # 1 of 50
        self.__start_health = start_health #100

    @staticmethod
    def print_score():
        print("Hello")

    def get_sex(self):
        return self.sex

    def set_sex(self, sex):
        self.sex = sex #male or female
    @property
    def start_level(self):
        return self.__start_level

    @start_level.setter
    def start_level(self):
        self.__start_level= 1

    @property
    def start_health(self):
        return self.__start_health

    @start_health.setter
    def start_health(self):
        self.__start_health = 100

    def show_info(self):
        print(f"Sex: {self.__sex} Level: {self.__start_level} Health: {self.__start_health}")

class Gnome(Races):
    def __init__(self, sex, start_level, start_health, height, name,):
        super().__init__(sex,start_level, start_health)
        self.__height = height # 3 on scale of 1:10
        self.name = name

    def __str__(self):
        return "Gnome"

    def gnome_func(self):
        self.__str__()
        # return self.speed_increase #by 3x for 5 sec.



gnome1 = Gnome("Male", 1, 100, 3, "Gadget")
print(gnome1)

class Human(Races):
    def __init__(self, sex, start_level, start_health, height, name):
        super().__init__(sex, start_level, start_health)
        self.__height = height # 7 on scale of 1:10
        self.name = name

# human1 = Human("")

class Elf(Races):
    def __init__(self, sex, start_level, start_health, height, name):
        super().__init__(sex, start_level, start_health)
        self.__height = height # 9 on scale of 1:10
        self.name = name

# Races.get_sex()
Races.print_score()
gnome1.print_score()
gnome1.gnome_func()

