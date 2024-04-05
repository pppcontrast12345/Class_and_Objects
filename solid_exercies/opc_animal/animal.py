from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.__class__.__name__.lower()


    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):

    def make_sound(self):
        return "meow"


class Dog(Animal):

    def make_sound(self):
        return "woof-woof"


class Cow(Animal):

    def make_sound(self):
        return "muuuu"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Cow()]
animal_sound(animals)

