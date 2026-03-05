from collections import deque


class Node:
    def __init__(self, wert):
        self.wert = wert
        self.links = None
        self.rechts = None


def bfs_baum(root):
    if not root:
        return

    # Die Warteschlange mit dem Startknoten füllen
    queue = deque([root])

    while queue:
        # Den vordersten Knoten aus der Schlange nehmen
        aktuell = queue.popleft()
        print(f"Besuche Ebene: {aktuell.wert}")

        # Die Kinder hinten an die Schlange anstellen
        if aktuell.links:
            queue.append(aktuell.links)
        if aktuell.rechts:
            queue.append(aktuell.rechts)


# Baum-Struktur (wie bei DFS)
root = Node(1)
root.links = Node(2)
root.rechts = Node(3)
root.links.links = Node(4)

bfs_baum(root)
# Ausgabe: 1, 2, 3, 4 (DFS hätte 1, 2, 4, 3 ausgegeben)


def finde_kurzesten_weg(labyrinth, start_zeile, start_spalte):
    # 1. VORBEREITUNG
    anzahl_zeilen = len(labyrinth)
    anzahl_spalten = len(labyrinth[0])

    # Die Warteschlange speichert: (Aktuelle_Zeile, Aktuelle_Spalte, Schritte_bisher)
    # Wir starten bei 0 Schritten.
    warteschlange = deque([(start_zeile, start_spalte, 0)])

    # Das "Gedächtnis", damit wir nicht im Kreis laufen
    besucht = set([(start_zeile, start_spalte)])

    # 2. DIE SUCH-SCHLEIFE (Solange noch Wege offen sind...)
    while warteschlange:
        # Nimm den ältesten Eintrag (First In, First Out)
        aktuelle_z, aktuelle_s, schritte = warteschlange.popleft()

        # PRÜFUNG: Sind wir am Ziel? (Unten rechts)
        if aktuelle_z == anzahl_zeilen - 1 and aktuelle_s == anzahl_spalten - 1:
            return f"Ziel erreicht in {schritte} Schritten!"

        # 3. NACHBARN ERKUNDEN (Oben, Unten, Links, Rechts)
        moegliche_richtungen = [
            (aktuelle_z + 1, aktuelle_s),  # Runter
            (aktuelle_z - 1, aktuelle_s),  # Hoch
            (aktuelle_z, aktuelle_s + 1),  # Rechts
            (aktuelle_z, aktuelle_s - 1),  # Links
        ]

        for n_zeile, n_spalte in moegliche_richtungen:
            # Check: Ist der Nachbar im Gitter, keine Wand (0) und unbesucht?
            ist_im_gitter = (
                0 <= n_zeile < anzahl_zeilen and 0 <= n_spalte < anzahl_spalten
            )

            if (
                ist_im_gitter
                and labyrinth[n_zeile][n_spalte] == 0
                and (n_zeile, n_spalte) not in besucht
            ):
                # Markieren als besucht (bevor wir ihn in die Schlange legen!)
                besucht.add((n_zeile, n_spalte))
                # Ab in die Warteschlange für die nächste "Welle"
                warteschlange.append((n_zeile, n_spalte, schritte + 1))

    return "Kein Weg zum Ziel gefunden."


# TEST-DATEN
mein_labyrinth = [[0, 1, 0, 0], [0, 0, 0, 1], [1, 1, 0, 0], [0, 0, 1, 0]]

ERGEBNISE = finde_kurzesten_weg(mein_labyrinth, 0, 0)
print(ERGEBNISE)
