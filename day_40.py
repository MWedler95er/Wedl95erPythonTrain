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
    def pet_sound(self):
        return "Woof, Woof!"

class Cat(Pets):
    def pet_sound(self):
        return "Meow, Meow!"
    
class Bird(Pets):
    def pet_sound(self):
        return "Chirp, Chirp!"
    
my_dog = Dog("Buddy", "Dog", 5)
my_cat = Cat("Whiskers", "Cat", 3)
my_bird = Bird("Tweety", "Bird", 2)

print(my_dog.pet_info())
print(my_dog.pet_sound())

print(my_cat.pet_info())
print(my_cat.pet_sound())

print(my_bird.pet_info())
print(my_bird.pet_sound())