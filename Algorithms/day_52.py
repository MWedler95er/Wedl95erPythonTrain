"""DAY 52  - Hash tables
item scanner
"""


class ItemScanner:
    def __init__(self):
        self.items = [None] * 13

    def add_item(self, item_name, item_beschreibung):
        # print(hash(item_name)% len(self.items))
        self.items[hash(item_name) % len(self.items)] = item_beschreibung

    def get_item_beschreibung(self, item_name):
        index = hash(item_name) % len(self.items)
        if self.items[index] is not None:
            return self.items[index]
        return "Item nicht gefunden."


programm = ItemScanner()
programm.add_item("Schwert", "Ein scharfes Schwert aus Stahl.")
programm.add_item("Schild", "Ein starker Schild aus Holz und Eisen.")
programm.add_item("Trank", "Ein heilender Trank, der Wunden heilt.")

print(programm.get_item_beschreibung("Schwert"))
print(programm.get_item_beschreibung("Schild"))
print(programm.get_item_beschreibung("Trank"))
print(programm.get_item_beschreibung("Bogen"))
