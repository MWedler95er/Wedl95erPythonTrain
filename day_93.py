import cProfile
import sys
import timeit

# ============================================================
# SCHRITT 1: PROFILING — Variante A vs B messen
# ============================================================


def variante_a():
    ergebnis = []
    for zahl in range(1000):
        ergebnis.append(zahl * 2)
    return ergebnis


def variante_b():
    return [zahl * 2 for zahl in range(1000)]


zeit_a = timeit.timeit(variante_a, number=10000)
zeit_b = timeit.timeit(variante_b, number=10000)

print(f"Variante A (for + append): {zeit_a:.4f} Sekunden")
print(f"Variante B (list comprehension): {zeit_b:.4f} Sekunden")
print(f"Variante B ist {zeit_a / zeit_b:.2f}x schneller")

# ============================================================
# SCHRITT 2: ALGORITHMEN — list vs set
# ============================================================

daten_list = list(range(100000))  # Liste mit 100.000 Zahlen
daten_set = set(range(100000))  # Set mit 100.000 Zahlen


def suche_list():
    return 99999 in daten_list  # Sucht von vorne bis hinten


def suche_set():
    return 99999 in daten_set  # Direkte Berechnung


zeit_list = timeit.timeit(suche_list, number=10000)
zeit_set = timeit.timeit(suche_set, number=10000)

print(f"Liste suchen:  {zeit_list:.4f} Sekunden")
print(f"Set suchen:    {zeit_set:.4f} Sekunden")
print(f"Set ist {zeit_list / zeit_set:.0f}x schneller")

# ============================================================
# SCHRITT 3: cProfile — ganzes Programm analysieren
# ============================================================


def langsame_funktion():
    summe = 0
    for i in range(100000):
        summe += i
    return summe


def schnelle_funktion():
    return sum(range(100000))  # Pythons eingebautes sum()


def hauptprogramm():
    for _ in range(50):
        langsame_funktion()
    for _ in range(50):
        schnelle_funktion()


cProfile.run("hauptprogramm()")

# ============================================================
# SCHRITT 4: GENERATOR — Speicher sparen
# ============================================================

# Liste: alle Werte sofort im Speicher
liste = [zahl * 2 for zahl in range(100000)]

# Generator: Werte werden erst bei Bedarf berechnet
generator = (zahl * 2 for zahl in range(100000))

print(f"Liste Speicher:     {sys.getsizeof(liste):>10} Bytes")
print(f"Generator Speicher: {sys.getsizeof(generator):>10} Bytes")
