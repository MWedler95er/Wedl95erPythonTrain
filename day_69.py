import pandas as pd

# Datensatz laden
df = pd.read_csv("games_march2025_cleaned_201.csv")

# release_date wieder in datetime umwandeln, falls nötig
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
df["release_year"] = df["release_date"].dt.year

# 1) Basis-Statistiken für numerische Spalten
numeric_summary = df.describe()  # count, mean, std, min, 25%, 50%, 75%, max
print("=== Basis-Statistiken (numerische Spalten) ===")
print(numeric_summary)

# 2) Spezielle Kennzahlen für ausgewählte Spalten
cols_of_interest = [
    "price",
    "average_playtime_2weeks",
    "average_playtime_forever",
]
for col in cols_of_interest:
    if col in df.columns:
        series = df[col].dropna()
        print(f"\n=== Statistik für Spalte: {col} ===")
        print(f"Anzahl Werte: {series.count():.0f}")
        print(f"Mittelwert:  {series.mean():.2f}")
        print(f"Median:      {series.median():.2f}")
        print(f"Standardabw: {series.std():.2f}")
        print(f"Minimum:     {series.min():.2f}")
        print(f"Maximum:     {series.max():.2f}")

# 3) Korrelationen zwischen numerischen Spalten
print("\n=== Korrelationsmatrix (numerische Spalten) ===")
corr = df.corr(numeric_only=True)
print(corr)

# Beispiel: Korrelation zwischen Preis und Gesamtspielzeit
if {"price", "average_playtime_forever"}.issubset(df.columns):
    sub = df[["price", "average_playtime_forever"]].dropna()
    price_play_corr = sub["price"].corr(sub["average_playtime_forever"])
    print("\nKorrelation Preis vs. Gesamt-Spielzeit:", round(price_play_corr, 3))

# 4) Vergleich von Gruppen: z.B. „billige“ vs „teure“ Spiele
if "price" in df.columns and "average_playtime_forever" in df.columns:
    # Schwelle definieren (z.B. Medianpreis)
    price_median = df["price"].median()
    cheap = df[df["price"] <= price_median]["average_playtime_forever"].dropna()
    expensive = df[df["price"] > price_median]["average_playtime_forever"].dropna()

    print("\n=== Vergleich billige vs. teure Spiele (nach Gesamtspielzeit) ===")
    print(f"Medianpreis im Datensatz: {price_median:.2f}")
    print(f"Billige Spiele - Mittelwert Spielzeit:  {cheap.mean():.2f}")
    print(f"Teure Spiele   - Mittelwert Spielzeit:  {expensive.mean():.2f}")
