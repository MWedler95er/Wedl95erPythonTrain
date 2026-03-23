import numpy as np
import pandas as pd

# --- Daten laden (wie in day_69) ---
df = pd.read_csv("games_march2025_cleaned_201.csv")
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
df["release_year"] = df["release_date"].dt.year

# Wir wählen ein paar numerische Spalten
cols = ["price", "average_playtime_2weeks", "average_playtime_forever"]
for c in cols:
    if c not in df.columns:
        raise ValueError(f"Spalte {c} fehlt im Datensatz")

# NaN entfernen, damit NumPy gut arbeiten kann
numeric_df = df[cols].dropna()

# --- 1) Pandas -> NumPy-Arrays ---
price = numeric_df["price"].to_numpy()
play_2w = numeric_df["average_playtime_2weeks"].to_numpy()
play_forever = numeric_df["average_playtime_forever"].to_numpy()

print("=== NumPy Arrays: Shapes ===")
print("price:", price.shape)
print("play_2w:", play_2w.shape)
print("play_forever:", play_forever.shape)

# --- 2) Basis-Statistiken mit NumPy ---
print("\n=== Basis-Statistiken (NumPy) ===")
print("Preis - Mittelwert:", np.mean(price))
print("Preis - Median:", np.median(price))
print("Preis - Std:", np.std(price, ddof=1))  # ddof=1 -> Stichproben-Std
print("Preis - Min:", np.min(price))
print("Preis - Max:", np.max(price))

# Vergleich mit Pandas (nur als Kontrolle)
print("\n(Pandas zum Vergleich)")
print(numeric_df["price"].describe())

# --- 3) Boolesche Masken & Filtern mit NumPy ---
print("\n=== Boolesche Masken ===")
# Beispiel: alle Spiele mit Preis > 20
mask_expensive = price > 20
print("Anzahl teurer Spiele (>20):", np.sum(mask_expensive))

expensive_prices = price[mask_expensive]
print("Mittelwert Preis (nur teuer):", np.mean(expensive_prices))

# Beispiel: Spiele mit viel Spielzeit (forever > 100h) und gleichzeitig billig (Preis < 10)
mask_longplay = play_forever > 100
mask_cheap = price < 10
mask_good_deal = mask_longplay & mask_cheap

print("Anzahl 'good deals' (viel Spielzeit & billig):", np.sum(mask_good_deal))

# --- 4) Vektorisierte Berechnungen ---
print("\n=== Vektorisierte Berechnungen ===")
# z.B. 'Preis pro Stunde' auf Basis Gesamtspielzeit
# Um Division durch 0 zu vermeiden, setzen wir 0-Spielzeit auf np.nan
play_forever_safe = play_forever.copy().astype(float)
play_forever_safe[play_forever_safe == 0] = np.nan

price_per_hour = price / play_forever_safe  # vektorisiert
print("Preis pro Stunde - Beispielwerte (erste 10):")
print(price_per_hour[:10])

# Zusätzliche Kontrolle: Preis, Spielzeit, Preis/Stunde nebeneinander
print("\nBeispiele (Preis, Spielzeit, Preis pro Stunde):")
for p, t, pph in zip(price[:10], play_forever_safe[:10], price_per_hour[:10]):
    print(f"Preis={p:.2f}, Spielzeit={t}, Preis/Stunde={pph}")

# Kennzahlen für Preis pro Stunde (NaN ignorieren)
print("Mittelwert Preis pro Stunde:", np.nanmean(price_per_hour))
print("Median Preis pro Stunde:", np.nanmedian(price_per_hour))

# --- 5) Korrelation mit NumPy ---
print("\n=== Korrelation (NumPy) ===")
# Korrelation zwischen Preis und Gesamtspielzeit
# np.corrcoef liefert Matrix; [0,1] ist die Korrelation der beiden Vektoren
corr_matrix = np.corrcoef(price, play_forever)
price_play_corr = corr_matrix[0, 1]
print("Korrelation Preis vs. Gesamtspielzeit:", price_play_corr)

# --- 6) Einfache lineare Regression (NumPy) ---
print("\n=== Einfache lineare Regression (NumPy) ===")
# Wir modellieren: play_forever ≈ a * price + b
# Lösung per least squares: [a, b] = argmin ||X*[a,b] - y||²
X = np.column_stack([price, np.ones_like(price)])  # Design-Matrix: [price, 1]
y = play_forever

# np.linalg.lstsq gibt a,b so zurück, dass X @ [a,b] bestmöglich y approximiert
coeffs, residuals, rank, s = np.linalg.lstsq(X, y, rcond=None)
a, b = coeffs

print(f"Geschätztes Modell: play_forever ≈ {a:.4f} * price + {b:.4f}")
print("Sum of squared residuals:", residuals)

# Beispielvorhersage: erwartete Spielzeit für ein Spiel mit Preis 10
EXAMPLE_PRICE = 10.0
predicted_play = a * EXAMPLE_PRICE + b
print(
    f"Erwartete Gesamtspielzeit für Preis {EXAMPLE_PRICE}: {predicted_play:.2f} (Stunden?)"
)

# --- 7) Mehrdimensionale Arrays ---
print("\n=== Mehrdimensionale Arrays ===")
# Wir kombinieren die drei Spalten in ein 2D-Array (N x 3)
data_matrix = np.column_stack([price, play_2w, play_forever])
print("data_matrix shape:", data_matrix.shape)

# Spaltenweiser Mittelwert / Std
col_means = np.mean(data_matrix, axis=0)
col_std = np.std(data_matrix, axis=0, ddof=1)
print("Spaltenmittelwerte [price, play_2w, play_forever]:", col_means)
print("Spalten-Std:", col_std)

# Zeilenweise Operation: z.B. normierte Werte je Zeile (nur als Demo)
# WARNUNG: Das ist hier inhaltlich nicht unbedingt sinnvoll, aber gut zum Üben:
row_sums = np.sum(data_matrix, axis=1, keepdims=True)
# Division durch 0 vermeiden
row_sums[row_sums == 0] = 1
row_normalized = data_matrix / row_sums
print("Erste 3 Zeilen normiert:")
print(row_normalized[:3])
