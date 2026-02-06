import random
import dataclasses

@dataclasses.dataclass
class Player():
    name: str
    health: int = 3
    krit_chance: float = 0.2


class RussischRollette():
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

    def shoot(self, Player):
        bullet = self.pop()
        if bullet== 1:
            if random.random() < Player.krit_chance:
                Player.health -= 2
                return "Kritischer Treffer! BANG!"
            else:
                Player.health -= 1
                return "BANG!"
        else:
            return "Klick! Glück gehabt."
        
    def game_start(self, **kwargs):
        while True:
            for player in kwargs.values():
                result = self.shoot(player)
                print(f"{player.name} schießt: {result} (Health: {player.health})")
                if player.health <= 0:
                    print("="*50)
                    print(f"{player.name} ist ausgeschieden!")
                    print("="*50)
                    return
                if self.stapel is None and Player.health != 0:
                    print("Alle Kugeln wurden abgefeuert. Das Spiel endet unentschieden.")
                    return
        
        
PL1= Player(name="Player1")
PL2 = Player(name="Player2")

game = RussischRollette()
game.load_bullet()
print(game.game_start(PL1=PL1, PL2=PL2))