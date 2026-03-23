import matplotlib.pyplot as plt
import pandas as pd

_csv = pd.read_csv("games_march2025_cleaned_201.csv")

_csv["release_date"] = pd.to_datetime(_csv["release_date"], errors="coerce")
_csv["release_year"] = _csv["release_date"].dt.year


# --- Testdiagramm, um Matplotlib zu verstehen ---
# Eine einfache Linie: x-Werte und y-Werte
x = [1, 2, 3, 4, 5]
y = [1, 14, 9, 16, 25]

plt.figure()  # Neue Grafik starten
plt.plot(x, y)  # Linie zeichnen
plt.title("Test-Diagramm")  # Titel
plt.xlabel("x-Werte")  # Beschriftung x-Achse
plt.ylabel("y-Werte")  # Beschriftung y-Achse
plt.tight_layout()  # Layout etwas schöner machen
plt.show()  # grafik aufrufen
plt.savefig("test_plot.png")  # grafik speichern


# --- Diagramm 1: Histogramm der Release-Jahre ---
# Wir nehmen nur gültige Jahre (keine NaN)
years = _csv["release_year"].dropna().astype(int)

plt.figure()
plt.hist(years, bins=25)  # bins -> jahresgruppen
plt.title("Anzahl Spiele pro Erscheinungsjahr")
plt.xlabel("Erscheiungsjahr")
plt.ylabel("Anzahl Spiele")
plt.tight_layout()
plt.savefig("games_per_year.png")


# --- Diagramm 2: Top 10 Publisher nach Anzahl Spiele ---
publisher_counts = (
    _csv.groupby("publishers")["name"].count().sort_values(ascending=False).head(10)
)


# Jeder Series/DataFrame hat eine .plot()-Methode
# Pandas hat eine eingebaute Plot-Funktion, die auf Matplotlib basiert.

# publisher_counts.plot(...) sagt: „male diese Daten als Diagramm“.
# Standard wäre ein Liniendiagramm, deshalb geben wir kind="bar" an.

# Was bedeutet kind="bar"?
# kind legt die Diagramm-Art fest:

# kind="line" → Liniendiagramm (Standard)
# kind="bar" → vertikales Balkendiagramm
# kind="barh" → horizontale Balken
# kind="hist" → Histogramm
# kind="pie" → Tortendiagramm


plt.figure()
publisher_counts.plot(kind="bar")
plt.title("Top 10 Publisher nach Anzahl Spiele")
plt.xlabel("Publisher")
plt.ylabel("Anzahl Spiele")
plt.xticks(rotation=45, ha="right")  # Labels lesbarer machen
plt.tight_layout()
plt.savefig("top_10pub_.png")


# --- Diagramm 3: Top 10 Spiele nach Spielzeit (letzte 2 Wochen) ---
top_10_games = _csv.sort_values("average_playtime_2weeks", ascending=False).head(10)
print(top_10_games[["name", "average_playtime_2weeks"]])

plt.figure()
plt.barh(top_10_games["name"], top_10_games["average_playtime_2weeks"])
plt.title("Top 10 Games nach Speilzeit der letzten zwei wochen")
plt.xlabel("Spiele")
plt.ylabel("Spielzeit (zwei wochen)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("top_10_game_two_weeks.png")


# --- Diagramm 4: Preis vs. Gesamt-Spielzeit (falls Spalten vorhanden) ---
if "price" in _csv.columns and "average_playtime_forever" in _csv.columns:
    plt.figure()
    plt.scatter(_csv["price"], _csv["average_playtime_forever"], alpha=0.3)
    plt.title("Preis vs. Gesamt-Spielzeit")
    plt.xlabel("Preis")
    plt.ylabel("Spielzeit gesamt")
    plt.tight_layout()
    plt.savefig("vs_grafik.png")
