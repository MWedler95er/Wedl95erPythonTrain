import pandas
kunden_df = pandas.read_csv("kunden.csv")
best_df = pandas.read_csv("bestellungen.csv")

zahlen = pandas.Series([10.2,120.7,30.0], name="punkte")  # Key - Value 
print(zahlen)
print("___________________________")

daten = {
    "name": ["Anna", "Bob", "Chris", "Lars", "Susi", "Micha"],
    "alter": [20,20,20,20,20,20],
    "herkunft": ["de", "eng", "esp","de", "eng", "esp"]
}
df = pandas.DataFrame(daten) # "exel" -> list format
print(df)


"""
print(df.head(4))       # erste Zeilen( bestimmt anzahl der ausgeeben reihen)
print(df.tail(2))       # letzte Zeilen ( -"- )
print("___________________________")
print(df.shape)        # (Zeilen, Spalten) -> ( 3 "zeilen" , 4 "spalten")
print("___________________________")
print(df.columns)      # Spaltennamen 
print("___________________________")
print(df.info())       # Datentypen + Null-Werte
print("___________________________")
print(df.describe())   # Statistiken für numerische Spalten
"""

print("wie viele Zielen und Spalten hat die CSV ? ")
print(kunden_df.shape)
print("Welche Spalten gibt es?")
print(kunden_df.columns)
print("Gibt es fehlende Werte?")
print(kunden_df.info())



df_alter = kunden_df[kunden_df["alter"] > 30][["name", "alter"]]
print(df_alter)
print("________________________")


#print(kunden_df[kunden_df["alter"] > 30])
#print(kunden_df[kunden_df["stadt"] == "Berlin"])
#print(kunden_df[(kunden_df["alter"] > 30) & (kunden_df["stadt"] == "Berlin")])


#print(kunden_df.iloc[0:5])
#print(kunden_df.loc[0:5, ["name", "alter"]])


#kunden_df["alter_plus_10"] = kunden_df["alter"] +10
#print(kunden_df)

#kunden_df["ist_alt"] = kunden_df["alter"] > 40
#print(kunden_df)

#kunden_df = kunden_df.drop(columns=["alter_plus_10"])

#print(kunden_df.groupby("name")["umsatz_2023"].mean())
#print(kunden_df.groupby("stadt")["umsatz_2023"].sum())
#print(kunden_df.groupby("stadt")["umsatz_2023"].agg(["min", "max", "mean"]))
#print(kunden_df.groupby(["stadt", "land"])["umsatz_2024"].sum())
"""
print("durchschnitsalter pro Stadt")
print(kunden_df.groupby("stadt")["alter"].mean())

print("Gesamt umsatz pro person")
kunden_df["gesamt_umsatz"] = kunden_df["umsatz_2023"] + kunden_df["umsatz_2024"]
print(kunden_df.groupby("name")["gesamt_umsatz"].sum())
"""

print("anzahl der None einträge in kunden.csv")
print(kunden_df.isna().sum())
print("Entsheide pro spalte: löschenode auffüllen?")
#df_dropt = kunden_df.dropna() #löscht alle einträge die NaN haben 
df_dropt = kunden_df.dropna(axis="columns") 
#löscht alle einträge die NaN haben wen (leer) mögliche konfiguration möglich (axis= 0/index or 1/columns or any or all)
print(df_dropt)

#kunden_df["umsatz_2023"] = kunden_df["umsatz_2023"].fillna(kunden_df["umsatz_2023"].mean())
# "umsatz_2023" aufruf = "umsatz_2023" aufruf . befüllen mit avg "umsatz_2023" 
#kunden_df["umsatz_2024"] = kunden_df["umsatz_2024"].fillna(kunden_df["umsatz_2024"].mean())

print(kunden_df.sort_values("alter", ascending=False))



kunden = pandas.read_csv("kunden.csv")
bestellungen = pandas.read_csv("bestellungen.csv")

df_join = pandas.merge(bestellungen, kunden, on="kunden_id", how="left")

print(df_join)