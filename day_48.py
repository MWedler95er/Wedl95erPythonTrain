class Warteschlange:
    def __init__(self, name: str):
        self.name = name
        self.queue = []

    def anstellen(self, person: str):
        self.queue.append(person)

    def bedienung(self) -> str:
        if not self.ist_leer():
            self.queue.pop(0)
            print("Kunde bedient.")
            return self.name

    def ist_leer(self) -> bool:
        return len(self.queue) == 0

    def wer_ist_als_nächstes_dran(self) -> str:
        if not self.ist_leer():
            return self.queue[0]
        else:
            return "Die Warteschlange ist leer."


warteschlange = Warteschlange("Supermarkt")
warteschlange.anstellen("Person XYZ")
warteschlange.anstellen("Person 123")
warteschlange.anstellen("Person 0815")
print(warteschlange.wer_ist_als_nächstes_dran())
warteschlange.bedienung()
print(warteschlange.wer_ist_als_nächstes_dran())
warteschlange.bedienung()
print(warteschlange.wer_ist_als_nächstes_dran())
warteschlange.bedienung()
print(warteschlange.wer_ist_als_nächstes_dran())
