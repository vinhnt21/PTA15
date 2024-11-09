"""
Class Dog
- Attributes: name, age, color
- Methods: bark, run, sleep
"""


class Dog:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def bark(self):
        print(f"{self.name} is barking.")

    def run(self):
        print(f"{self.name} is running.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


lulu = Dog("Lulu", 2, "black")
lulu.bark()

mimi = Dog("Mimi", 3, "white")
mimi.bark()
