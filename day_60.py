def hanoi(anzahl, von, temp, ziel, ebene=0):
    print("")
    if anzahl > 0:
        # Einrückung zeigt uns, wie tief wir in der Rekursion sind
        einrueckung = "_." * ebene

        hanoi(anzahl - 1, von, ziel, temp, ebene + 1)

        print(f"{einrueckung}Aktion: Scheibe {anzahl} von {von} zu {ziel}")

        hanoi(anzahl - 1, temp, von, ziel, ebene + 1)


hanoi(4, "A", "B", "C")

"""
def hanoi_versuche(anzahl, von, temp, ziel, w_satz, ebene=0):
    print(w_satz)
    if anzahl > 0:
        # Einrückung zeigt uns, wie tief wir in der Rekursion sind
        einrueckung = "_." * ebene

        hanoi_versuche(anzahl-1, von, ziel, temp, w_satz, ebene + 1)

        print(f"{einrueckung}Aktion: Scheibe {anzahl} von {von} zu {ziel}")

        hanoi_versuche(anzahl-1, temp, von, ziel, w_satz, ebene + 1)


versuchs_satz = "Das ist ein Satz"
wörter_satz = versuchs_satz.split()
hanoi_versuche(len(wörter_satz),'A','B','C',wörter_satz)

"""
