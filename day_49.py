class Node:
    def __init__(self):
        self.value = 50
        self.left = None
        self.right = None


class HigherLowerGame:
    def __init__(self):
        self.root = Node()
        self.guesses = []

    def _guess_einfuegen(self, aktueller_knoten: Node, guess: int):
        if guess < aktueller_knoten.value:
            if aktueller_knoten.left is None:
                aktueller_knoten.left = Node()
                aktueller_knoten.left.value = guess
            else:
                self._guess_einfuegen(aktueller_knoten.left, guess)
            return "Lower"
        if guess > aktueller_knoten.value:
            if aktueller_knoten.right is None:
                aktueller_knoten.right = Node()
                aktueller_knoten.right.value = guess
            else:
                self._guess_einfuegen(aktueller_knoten.right, guess)
            return "Higher"
        return "Winner"

    def guess(self, guess):
        result = self._guess_einfuegen(self.root, guess)
        self.guesses.append((guess, result))
        return result

    def print_guesses(self):
        print("\n=== All Guesses ===")
        for guess, result in self.guesses:
            print(f"Guess: {guess}, Result: {result}")


game = HigherLowerGame()
print(f"Game started. Root value: {game.root.value}")
print(f"Guess 30: {game.guess(30)}")
print(f"Guess 70: {game.guess(70)}")
print(f"Guess 40: {game.guess(40)}")
print(f"Guess 60: {game.guess(60)}")
print(f"Guess 50: {game.guess(50)}")
game.print_guesses()
