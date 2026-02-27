import random

class Kartendeck:
    """Repräsentiert ein Kartendeck und steuert ein einfaches Blackjack-Spiel.
    Verwaltet Karten, Spieler- und Bankhände sowie den Ablauf einer Spielrunde.

    Args:
        None

    """
    def __init__(self):
        self.karten_werte = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Bube", "Dame", "König", "Ass"]
        self.karten_farben = ["❤️", "♠️", "♦️", "♣️"]
        self.karten_deck = [[w, f] for f in self.karten_farben for w in self.karten_werte]
        self.index = 0
        self.spieler_hand = []
        self.bank_hand = []

    def __next__(self):
        if self.index < len(self.karten_deck):
            karte = self.karten_deck[self.index]
            self.index += 1
            return karte
        else:
            raise StopIteration

    def __iter__(self):
        self.index = 0
        return self

    def karten_mischen(self):
        random.shuffle(self.karten_deck)
        print("-|- Deck wurde frisch gemischt -|-")

    def austeilen(self):
        return self.karten_deck.pop(0) if self.karten_deck else None

    def wert_berechnen(self, hand):
        wert = 0
        asse = 0
        for karte, farbe in hand:
            if karte in ["Bube", "Dame", "König"]:
                wert += 10
            elif karte == "Ass":
                asse += 1
                wert += 11
            else:
                wert += karte
        
        while wert > 21 and asse > 0:
            wert -= 10
            asse -= 1
        return wert

    def bank_spielt(self, spieler_punkte):
        self.bank_hand = [self.austeilen(), self.austeilen()]
        
        while True:
            bank_punkte = self.wert_berechnen(self.bank_hand)
            hand_str = ", ".join([f"{k}{f}" for k, f in self.bank_hand])
            print(f"Bank Hand: {hand_str} (Punkte: {bank_punkte})")

            if bank_punkte < 17 or spieler_punkte>bank_punkte:
                print("Bank zieht noch eine Karte...")
                self.bank_hand.append(self.austeilen())
            else:
                break
        
        # --- Finaler Vergleich ---
        if bank_punkte > 21:
            print("Bank hat sich überkauft! DU GEWINNST!")
        elif bank_punkte > spieler_punkte:
            print("Bank gewinnt!")
        elif bank_punkte < spieler_punkte:
            print("Glückwunsch! Du hast die Bank geschlagen!")
        else:
            print("Unentschieden!")

    def game_logik(self):
        self.karten_mischen()
        self.spieler_hand = [self.austeilen(), self.austeilen()]
        
        while True:
            punkte = self.wert_berechnen(self.spieler_hand)
            hand_str = ", ".join([f"{k}{f}" for k, f in self.spieler_hand])
            print(f"\nDeine Hand: {hand_str} (Punkte: {punkte})")
            
            if punkte == 21:
                print("Blackjack! Du hast gewonnen!")
                return # Spiel beendet
            if punkte > 21:
                print("Über 21! Du hast leider verloren.")
                return # Spiel beendet

            wahl = input("Noch eine [K]arte ziehen oder [H]alten? ").lower()

            if wahl == 'k':
                neue_karte = self.austeilen()
                self.spieler_hand.append(neue_karte)
                print(f"Gezogen: {neue_karte[0]}{neue_karte[1]}")
            elif wahl == 'h':
                print(f"Du hältst bei {punkte} Punkten.")
                self.bank_spielt(punkte)
                break
            else:
                print("Ungültige Eingabe!")

spiel_deck = Kartendeck()

for x in spiel_deck:
    print(x)

spiel_deck.game_logik()