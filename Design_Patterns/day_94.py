# ============================================================
# SCHRITT 1: DECORATOR MIT PARAMETERN
# ============================================================


def logger(level):
    def decorator(funktion):
        def wrapper(*args, **kwargs):
            print(f"[{level}] Starte: {funktion.__name__}")
            ergebnis = funktion(*args, **kwargs)
            print(f"[{level}] Fertig: {funktion.__name__}")
            return ergebnis

        return wrapper

    return decorator


@logger(level="INFO")
def lieferung_speichern(kunde):
    print(f"  Speichere: {kunde}")


@logger(level="WARNING")
def lager_pruefen(bestand):
    if bestand < 10:
        print(f"  Bestand kritisch: {bestand} kg")


# --- Test ---
lieferung_speichern("Weber GmbH")
print()
lager_pruefen(5)

# ============================================================
# SCHRITT 2: DESCRIPTOR
# ============================================================


class PositiveZahl:
    """Descriptor: erlaubt nur positive Zahlen"""

    def __init__(self):
        self._name = ""

    def __set_name__(self, owner, name):
        self._name = name  # Speichert den Attributnamen

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, f"_{self._name}", None)

    def __set__(self, obj, wert):
        if wert < 0:
            raise ValueError(f"{self._name} kann nicht negativ sein: {wert}")
        setattr(obj, f"_{self._name}", wert)


class Lieferung:
    menge_kg = PositiveZahl()  # ← Descriptor wird als Klassenattribut gesetzt
    preis = PositiveZahl()

    def __init__(self, kunde, menge_kg, preis):
        self.kunde = kunde
        self.menge_kg = menge_kg  # ← ruft __set__ auf
        self.preis = preis


# --- Test ---
l1 = Lieferung("Weber GmbH", 120, 1.80)
print(f"{l1.kunde}: {l1.menge_kg} kg @ {l1.preis} €/kg")

try:
    l2 = Lieferung("Fehler GmbH", -50, 1.80)
except ValueError as e:
    print(f"Fehler: {e}")
