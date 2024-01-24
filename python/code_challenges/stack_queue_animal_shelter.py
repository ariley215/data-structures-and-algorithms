from data_structures.queue import Queue


class AnimalShelter:
    # set up the initial state of the AnimalShelter class with empty lists for dogs and cats
    def __init__(self):
        self.animals = []
        self.order = 0



class Dog:
    def __init__(self, name):
        self.species = "dog"
        self.name = name


class Cat:
    def __init__(self, name):
        self.species = "cat"
        self.name = name
