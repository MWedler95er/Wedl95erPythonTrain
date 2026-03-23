"""Day 82 — Tic-Tac-Toe"""

import dataclasses


@dataclasses.dataclass
class Player:
    """Repräsentiert einen Spieler mit Name, Symbol und Zugzähler."""

    name: str
    symbol: str  # "X" oder "O"
    moves: int = 0


class TicTacToe:  # pylint: disable=too-few-public-methods
    """Verwaltet Spielfeld, Spieler und Spielablauf für Tic-Tac-Toe."""

    FIELD_TEMPLATE = {
        "L-T": " ",
        "M-T": " ",
        "R-T": " ",
        "L-M": " ",
        "M-M": " ",
        "R-M": " ",
        "L-B": " ",
        "M-B": " ",
        "R-B": " ",
    }

    def __init__(self):
        self.players: list[Player] = []
        # jede neue Instanz bekommt ein leeres Spielfeld
        self.field: dict[str, str] = self.FIELD_TEMPLATE.copy()

    game_input = {
        1: "L-T",
        2: "M-T",
        3: "R-T",
        4: "L-M",
        5: "M-M",
        6: "R-M",
        7: "L-B",
        8: "M-B",
        9: "R-B",
    }

    # Reihenfolge der Felder für Darstellung (0–8)
    field_order = [
        "L-T",
        "M-T",
        "R-T",
        "L-M",
        "M-M",
        "R-M",
        "L-B",
        "M-B",
        "R-B",
    ]

    def _print_menu(self):
        """Show the main menu"""
        print("\n==== Tik-Tac-Toe Menü ====")
        print("(1) Spieler bennenen")
        print("(2) Spiel Starten")
        print("(3) Programm Stop")

    def menu(self) -> None:
        """Main menu of the application."""
        while True:
            self._print_menu()
            choice = input("Bitte wähle (1-3): ").strip()

            if choice == "1":
                self._handle_add_player()
            elif choice == "2":
                self._handel_game_start()
            elif choice == "3":
                print("Programm wird beendet.")
                break
            else:
                print("Ungültige Eingabe, bitte 1-3 wählen.")

    def _handle_add_player(self):
        self.players = []  # immer neu starten
        symbols = ["X", "O"]
        for i in range(2):
            name = input(f"\nPlayer {i + 1} Name: ")
            self.players.append(Player(name=name, symbol=symbols[i]))
        print("Spieler wurden angelegt. Zurück zum Menü.")

    def print_field(self):
        li = "-" * 13
        print("   L   M   R")
        print(li)
        print(
            " | "
            + self.field["L-T"]
            + " | "
            + self.field["M-T"]
            + " | "
            + self.field["R-T"]
            + " |  T"
        )
        print(li)
        print(
            " | "
            + self.field["L-M"]
            + " | "
            + self.field["M-M"]
            + " | "
            + self.field["R-M"]
            + " |  M"
        )
        print(li)
        print(
            " | "
            + self.field["L-B"]
            + " | "
            + self.field["M-B"]
            + " | "
            + self.field["R-B"]
            + " |  B"
        )
        print(li)

    def p_field(self):
        """Kompakte Version von print_field mit Schleife."""
        li = "-" * 13
        print("   L   M   R")
        print(li)

        row = []
        for idx, key in enumerate(self.field_order, start=1):
            # Symbol aus dem Spielfeld holen
            value = self.field[key]
            row.append(f" {value} ")

            # Wenn 3 Felder voll sind → Zeile drucken
            if idx % 3 == 0:
                print("|" + "|".join(row) + "|")
                print(li)
                row = []

    def _handel_game_start(self):
        if len(self.players) < 2:
            print("Bitte zuerst 2 Spieler anlegen (Menüpunkt 1).")
            return

        # Spielfeld zurücksetzen
        self.field = self.FIELD_TEMPLATE.copy()
        game_round = 0

        while True:
            current_player = self.players[game_round % 2]
            self.p_field()
            print(f"Am Zug: {current_player.name} ({current_player.symbol})")

            # Eingabe: L-M, m-t, l-b etc. -> alles egal, wird zu Großbuchstaben
            choice = input('Wähle ein Feld (z.B. "L-M" oder "m-t"): ').strip().upper()

            # prüfen, ob der Key existiert
            if choice not in self.FIELD_TEMPLATE:
                print('Ungültige Eingabe. Gültig sind z.B. "L-T", "M-M", "R-B"...')
                continue

            key = choice

            # prüfen, ob Feld frei ist
            if self.field[key] != " ":
                print("Feld ist schon belegt, anderes wählen.")
                continue

            # Zug setzen
            self.field[key] = current_player.symbol
            current_player.moves += 1
            game_round += 1

            # Sieg prüfen
            if self._check_winner(current_player.symbol):
                self.p_field()
                print(
                    f"Spieler {current_player.name} ({current_player.symbol}) hat gewonnen!"
                )
                break

            # Unentschieden?
            if game_round == 9:
                self.print_field()
                print("Unentschieden! Kein freies Feld mehr.")
                break

    def _check_winner(self, symbol: str) -> bool:
        f = self.field
        lines = [
            # Reihen
            ("L-T", "M-T", "R-T"),
            ("L-M", "M-M", "R-M"),
            ("L-B", "M-B", "R-B"),
            # Spalten
            ("L-T", "L-M", "L-B"),
            ("M-T", "M-M", "M-B"),
            ("R-T", "R-M", "R-B"),
            # Diagonalen
            ("L-T", "M-M", "R-B"),
            ("R-T", "M-M", "L-B"),
        ]

        for a, b, c in lines:
            if f[a] == f[b] == f[c] == symbol:
                return True
        return False


if __name__ == "__main__":
    game = TicTacToe()
    game.menu()
