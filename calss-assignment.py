class Enemy : 
    city: str

    def __init__(self, a, b, c):
        self.__name = a
        self.health = b
        self.attack = c


    def talk(self):
        print(f"Hello {self.__name}!")
enemy = Enemy("Goblin", 100, 10)

class Animal :
    def __init__(self, d, e):
        self.__name = d
        self.__species = e

    def talk(self):
        print(f"Hello {self.__name} the {self.__species}!")


class Dog(Animal, Enemy):
    def __init__(self, name, species, a, b, c):
        Animal.__init__(self, name, species)
        Enemy.__init__(self, a, b, c)

    def bark(self):
        print(f"{self.__name} says Woof!")