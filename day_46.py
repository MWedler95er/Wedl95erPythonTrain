import dataclasses


@dataclasses.dataclass
class Heros:
    name: str
    power: str
    power_level: int
    age: int
    universe: str
    voice_line: str


@dataclasses.dataclass
class Villains:
    name: str
    power: str
    power_level: int
    age: int
    universe: str
    voice_line: str


class SuperHumans(Heros, Villains):
    def say_voice_line(self):
        return f"{self.name} says: '{self.voice_line}'"

    def fight(self, opponent):
        if self.power_level > opponent.power_level:
            return f"{self.name} wins the fight against {opponent.name}!"
        if self.power_level < opponent.power_level:
            return f"{opponent.name} wins the fight against {self.name}!"
        return f"The fight between {self.name} and {opponent.name} is a draw!"


my_hero = Heros(
    "Superman",
    "Super Strength",
    35,
    400,
    "DC",
    "Truth, justice, and a better tomorrow.",
)
my_hero2 = Heros(
    "Spider Man",
    "Wall Crawling",
    25,
    300,
    "Marvel",
    "With great power comes great responsibility.",
)
my_villain = Villains("Joker", "Anarchy", 30, 250, "DC", "Why so serious?")
my_villain2 = Villains(
    "Thanos", "Infinity Gauntlet", 40, 500, "Marvel", "I am inevitable."
)


print(my_hero)
print(my_hero2)
print(SuperHumans.say_voice_line(my_hero))

print(SuperHumans.fight(my_hero, my_villain2))
