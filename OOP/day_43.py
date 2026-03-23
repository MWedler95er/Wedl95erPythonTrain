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
    def __init__(self, name, species, age, illnesses):
        super().__init__(name, species, age)
        self._illnesses = illnesses

    def pet_sound(self):
        return "Woof, Woof!"

    @property
    def illnesses(self):
        return self._illnesses

    @illnesses.setter
    def illnesses(self, new_illnesses):
        self._illnesses = new_illnesses


class Cat(Pets):
    def __init__(self, name, species, age, ill):
        super().__init__(name, species, age)
        self._illness = ill

    @property
    def illness(self):
        return self._illness

    @illness.setter
    def illness(self, new_illness):
        self._illness = new_illness

    def pet_sound(self):
        return "Meow, Meow!"


class Bird(Pets):
    def __init__(
        self,
        name,
        species,
        age,
        can_fly,
    ):
        super().__init__(name, species, age)
        self.can_fly = can_fly

    @property
    def illnesses(self):
        return self._illnesses

    @illnesses.setter
    def illnesses(self, new_illnesses):
        self._illnesses = new_illnesses

    def pet_sound(self):
        return "Chirp, Chirp!"


my_dog = Dog("Buddy", "Dog", 5, ["None"])
my_cat = Cat("Whiskers", "Cat", 3, ["Fleas", "Cold"])
my_bird = Bird("Tweety", "Bird", 2, True)

print(my_dog.pet_info())
print(my_dog.pet_sound())
print(my_dog.illnesses)


print(my_cat.pet_info())
print(my_cat.pet_sound())
print(my_cat.illness)

print(my_bird.pet_info())
print(my_bird.pet_sound())
