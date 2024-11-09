"""
Fish
- Attributes: name, color, price, specie
- Methods: swim, eat, sleep
"""
class Fish:
    def __init__(self, name, age, types):
        self.name = name
        self.age = age
        self.types = types

    def eat(self):
        print(f"{self.name} is eating")

    def swim(self):
        print(f"{self.name} is swimming.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


NeMo = Fish("LuLu", 8, "shark")
NeMo.swim()
MoMo = Fish("MoMo", 3, "Goby")
MoMo.eat()
