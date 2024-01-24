from data_structures.queue import Queue


class AnimalShelter:
    # set up the initial state of the AnimalShelter class with empty lists for dogs and cats
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()


class Animal:
    def __init__(self, name="unknown"):
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        species = "dog"


class Cat(Animal):
    def __init__(self, name):
        species = "cat"
