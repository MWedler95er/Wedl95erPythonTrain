# ============================================================
# PATTERN 1: SINGLETON
# ============================================================


class Datenbank:
    _instanz = None  # Klassenvariable — existiert nur einmal

    def __new__(cls):
        if cls._instanz is None:
            print("Neue Datenbankverbindung wird erstellt...")
            cls._instanz = super().__new__(cls)
        return cls._instanz

    def abfrage(self, sql):
        print(f"SQL ausgeführt: {sql}")


# --- Test ---
db1 = Datenbank()
db2 = Datenbank()

print(f"db1 ist db2: {db1 is db2}")  # Muss True sein!
db1.abfrage("SELECT * FROM kunden")

# ============================================================
# PATTERN 2: DECORATOR
# ============================================================


def logger(funktion):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starte: {funktion.__name__}")
        ergebnis = funktion(*args, **kwargs)
        print(f"[LOG] Fertig: {funktion.__name__}")
        return ergebnis

    return wrapper


@logger
def lieferung_speichern(kunde, menge):
    print(f"  Speichere: {kunde} — {menge} kg")


@logger
def rechnung_erstellen(kunde):
    print(f"  Erstelle Rechnung für: {kunde}")


# --- Test ---
lieferung_speichern("Weber GmbH", 120)
print()
rechnung_erstellen("Weber GmbH")

# ============================================================
# PATTERN 3: OBSERVER
# ============================================================


class Lieferung:
    def __init__(self):
        self._beobachter = []  # Liste aller angemeldeten Observer

    def anmelden(self, beobachter):
        self._beobachter.append(beobachter)

    def neue_lieferung(self, kunde, menge):
        print(f"\nNeue Lieferung: {kunde} — {menge} kg")
        for beobachter in self._beobachter:
            beobachter.aktualisieren(kunde, menge)


class Lager:
    def aktualisieren(self, menge):
        print(f"  [Lager] Bestand um {menge} kg erhöht")


class Buchhaltung:
    def aktualisieren(self, kunde):
        print(f"  [Buchhaltung] Rechnung für {kunde} erstellt")


class Email:
    def aktualisieren(self, kunde):
        print(f"  [Email] Bestätigung an {kunde} gesendet")


# --- Test ---
lieferung = Lieferung()

lieferung.anmelden(Lager())
lieferung.anmelden(Buchhaltung())
lieferung.anmelden(Email())

lieferung.neue_lieferung("Weber GmbH", 120)
lieferung.neue_lieferung("Fischer & Co", 85)

# ============================================================
# PATTERN 4: FACTORY
# ============================================================


class Aluminium:
    def verarbeiten(self):
        print("Aluminium wird eingeschmolzen (660°C)")


class Kupfer:
    def verarbeiten(self):
        print("Kupfer wird gereinigt und gepresst")


class Eisen:
    def verarbeiten(self):
        print("Eisen wird geschreddert")


class MaterialFactory:
    _materialien = {
        "aluminium": Aluminium,
        "kupfer": Kupfer,
        "eisen": Eisen,
    }

    @classmethod
    def erstellen(cls, material_typ):
        klasse = cls._materialien.get(material_typ.lower())
        if klasse is None:
            raise ValueError(f"Unbekanntes Material: {material_typ}")
        return klasse()


# --- Test ---
for material in ["Aluminium", "Kupfer", "Eisen", "Plastik"]:
    try:
        obj = MaterialFactory.erstellen(material)
        obj.verarbeiten()
    except ValueError as e:
        print(f"Fehler: {e}")
