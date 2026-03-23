import pandas as pd

# Datensatz laden
df = pd.read_csv("recycling_daten.csv")

# --- Erkunden ---
print("=== Erste 5 Zeilen ===")
print(df.head())

print("\n=== Datentypen & fehlende Werte ===")
print(df.info())

print("\n=== Statistiken der Zahlen-Spalten ===")
print(df.describe())

# ============================================================
# SCHRITT 2: DATA CLEANING
# ============================================================

# --- 2a: Fehlende Werte anzeigen ---
print("=== Fehlende Werte pro Spalte ===")
print(df.isnull().sum())

# --- 2b: Duplikate finden ---
print("\n=== Duplikate ===")
print(df[df.duplicated()])

# --- 2c: Ungültige Werte finden (negatives Gewicht) ---
print("\n=== Negative Mengen ===")
print(df[df["menge_kg"] < 0])

# ============================================================
# JETZT BEREINIGEN:
# ============================================================

# Zeilen mit negativer Menge entfernen
df = df[df["menge_kg"] >= 0]

# Duplikate entfernen (erste Kopie behalten)
df = df.drop_duplicates()

# Fehlende menge_kg mit dem Mittelwert auffüllen
mittelwert_menge = df["menge_kg"].mean()
df["menge_kg"] = df["menge_kg"].fillna(mittelwert_menge)

# Fehlende preis_pro_kg: mit dem Preis des gleichen Materials auffüllen
df["preis_pro_kg"] = df.groupby("material")["preis_pro_kg"].transform(
    lambda x: x.fillna(x.mean())
)

# Fehlende material-Einträge: mit "Unbekannt" füllen
df["material"] = df["material"].fillna("Unbekannt")

print("\n=== Nach Bereinigung: fehlende Werte ===")
print(df.isnull().sum())
print(f"\nNoch {len(df)} Zeilen übrig.")

# ============================================================
# SCHRITT 3: FEATURE ENGINEERING
# ============================================================

# --- 3a: Gesamtwert der Lieferung berechnen ---
df["gesamtwert_eur"] = df["menge_kg"] * df["preis_pro_kg"]

# --- 3b: Datum aufspalten in Jahr und Monat ---
df["datum"] = pd.to_datetime(df["datum"])
df["jahr"] = df["datum"].dt.year
df["monat"] = df["datum"].dt.month


# --- 3c: Lieferung kategorisieren nach Größe ---
def kategorisiere_lieferung(menge):
    if menge < 50:
        return "klein"
    if menge < 150:
        return "mittel"
    return "groß"


df["lieferung_groesse"] = df["menge_kg"].apply(kategorisiere_lieferung)

# --- Ergebnis anzeigen ---
print("=== Neue Spalten ===")
print(
    df[
        [
            "name",
            "material",
            "menge_kg",
            "preis_pro_kg",
            "gesamtwert_eur",
            "monat",
            "lieferung_groesse",
        ]
    ].to_string()
)

# ============================================================
# SCHRITT 4: AUSWERTUNG
# ============================================================

# --- 4a: Umsatz pro Material ---
print("=== Gesamtumsatz pro Material ===")
umsatz_material = (
    df.groupby("material")["gesamtwert_eur"].sum().sort_values(ascending=False)
)
print(umsatz_material.round(2))

# --- 4b: Umsatz pro Monat ---
print("\n=== Gesamtumsatz pro Monat ===")
umsatz_monat = df.groupby("monat")["gesamtwert_eur"].sum()
print(umsatz_monat.round(2))

# --- 4c: Durchschnittliche Liefergröße pro Stadt ---
print("\n=== Durchschnittliche Menge pro Ort ===")
menge_ort = df.groupby("ort")["menge_kg"].mean().sort_values(ascending=False)
print(menge_ort.round(1))

# --- 4d: Wie viele Lieferungen pro Größenklasse? ---
print("\n=== Anzahl Lieferungen pro Größenklasse ===")
print(df["lieferung_groesse"].value_counts())

# --- Datei speichern ---
df.to_csv("recycling_bereinigt.csv", index=False)
print("\n Bereinigte Datei gespeichert: recycling_bereinigt.csv")
