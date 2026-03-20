# pylint: skip-file
# mandelbrot.py


def mandelbrot(max_iter: int = 70, width: int = 120, height: int = 30):
    """
    Zeichnet eine einfache Mandelbrot-Menge als ASCII-Grafik in die Konsole.

    max_iter: wie oft z = z*z + c iteriert wird
    width:    Anzahl Spalten (x-Richtung)
    height:   Anzahl Zeilen (y-Richtung)
    """

    # Bereich in der komplexen Ebene, den wir anschauen
    # x von -2.0 bis 1.0, y von -1.0 bis 1.0 ist ein klassischer Ausschnitt
    x_min, x_max = -2.0, 1.0
    y_min, y_max = -1.0, 1.0

    # Zeichen für verschiedene "Fluchtgeschwindigkeiten"
    chars = " .:-=+*#%@0"

    for row in range(height):
        # y-Koordinate für diese Zeile berechnen (Zeile 0 = oben)
        # Wir gehen von y_max (oben) nach y_min (unten)
        y = y_max - (y_max - y_min) * row / (height - 1)
        # y ~ 0.931034
        line = ""
        for col in range(width):
            # x-Koordinate für diese Spalte berechnen
            x = x_min + (x_max - x_min) * col / (width - 1)

            # Komplexe Zahl c
            c = complex(x, y)
            z = 0 + 0j

            # Iteration
            iter_count = 0
            while abs(z) <= 2.0 and iter_count < max_iter:
                z = z * z + c
                iter_count += 1

            # Wähle ein Zeichen abhängig davon, wie schnell wir "abgehauen" sind
            if iter_count == max_iter:
                # vermutlich innerhalb der Mandelbrot-Menge
                ch = "0"
            else:
                # Skaliere iter_count auf die Zeichenliste
                idx = int(iter_count / max_iter * (len(chars) - 1))
                ch = chars[idx]

            line += ch
        print(line)


if __name__ == "__main__":
    mandelbrot()
