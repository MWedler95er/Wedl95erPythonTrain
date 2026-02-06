import dataclasses
import random


@dataclasses.dataclass
class Player:
    name: str
    health: int = 3
    krit_chance: float = 0.2


class RussischRollette:
    def __init__(self):
        self.stapel = []

    def push(self, item):
        self.stapel.append(item)

    def pop(self):
        if not self.stapel:
            raise IndexError("Stapel ist leer")
        return self.stapel.pop()

    def peek(self):
        if not self.stapel:
            raise IndexError("Stapel ist leer")
        return self.stapel[-1]

    def load_bullet(self):
        self.stapel = [random.randint(0, 1) for _ in range(10)]

    def shoot(self, player):
        bullet = self.pop()
        if bullet == 1:
            if random.random() < player.krit_chance:
                player.health -= 2
                return "Kritischer Treffer! BANG!"
            player.health -= 1
            return "BANG!"
        return "Klick! Glück gehabt."

    def game_start(self, **kwargs):
        if not kwargs:
            raise ValueError("Mindestens ein Spieler ist erforderlich!")

        round_num = 0
        while True:
            round_num += 1
            print(f"\n--- Runde {round_num} ---")

            for player in kwargs.values():
                if player.health <= 0:
                    continue

                if not self.stapel:
                    print("\n" + "=" * 50)
                    print(
                        "Alle Kugeln wurden abgefeuert. Das Spiel endet unentschieden."
                    )
                    print("=" * 50)
                    return

                result = self.shoot(player)
                print(f"{player.name} schießt: {result} (Health: {player.health})")

                if player.health <= 0:
                    print("\n" + "=" * 50)
                    print(f"{player.name} ist ausgeschieden!")
                    print("=" * 50)
                    alive_players = [p for p in kwargs.values() if p.health > 0]
                    if len(alive_players) <= 1:
                        if alive_players:
                            print(f"\n🎉 GEWINNER: {alive_players[0].name}!")
                        return


if __name__ == "__main__":
    PL1 = Player(name="🥶")
    PL2 = Player(name="🥵")

    game = RussischRollette()
    game.load_bullet()
    print("\n🔫 Russisches Roulette startet mit 2 Spielern!\n")
    game.game_start(PL1=PL1, PL2=PL2)
