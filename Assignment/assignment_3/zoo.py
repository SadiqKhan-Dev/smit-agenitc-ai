# Project Idea: Simple Zoo Management System 🐶🐱🦁

# Project Goal:

# Different animals add karo (Dog, Cat, Lion).

# Har animal ka sound play karo.

# Animal health/age ko safe store karo (encapsulation).

# Abstract class use karo base Animal ke liye.

# Polymorphism use karo sound() method ke liye.

from abc import ABC, abstractmethod

class Animal:
    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.health = health

    @abstractmethod
    def sound(self):
        pass
    
    def __str__(self):
        return f"{self.name} is {self.age} years old and has {self.health} health."

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Lion(Animal):
    def sound(self):
        return "Roar"
    

animals = [Dog("Buddy", 3, "good"), Cat("Whiskers", 2, "good"), Lion("Lion", 5, "good")]

for animal in animals:
    print(animal)
    print(animal.sound())