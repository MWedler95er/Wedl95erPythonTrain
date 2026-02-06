# Day 40 + 41

class Pets:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def pet_sound(self):
        raise NotImplementedError("Subclasses must implement this method. ")

    def pet_info(self):
        return f"{self.name} is a {self.species} and is {self.age} years old."


class Dog(Pets):
    def __init__(self, name, species, age, sex, aktive):
        super().__init__(name, species, age)
        self.sex = sex
        self.aktive = aktive

    def pet_sound(self):
        return "Woof, Woof!"


class Cat(Pets):
    def __init__(self, name, species, age, sex, ill):
        super().__init__(name, species, age)
        self.sex = sex
        self.ill = ill

    def pet_sound(self):
        return "Meow, Meow!"


class Bird(Pets):
    def __init__(self, name, species, age, sex, can_fly):
        super().__init__(name, species, age)
        self.sex = sex
        self.can_fly = can_fly

    def pet_sound(self):
        return "Chirp, Chirp!"


my_dog = Dog("Buddy", "Dog", 5, "Male", True)
my_cat = Cat("Whiskers", "Cat", 3, "Female", False)
my_bird = Bird("Tweety", "Bird", 2, "Female", True)

print(my_dog.pet_info())
print(my_dog.pet_sound())

print(my_cat.pet_info())
print(my_cat.pet_sound())

print(my_bird.pet_info())
print(my_bird.pet_sound())
