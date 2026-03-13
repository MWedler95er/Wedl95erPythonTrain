import pandas as pd

_csv = pd.read_csv("games_march2025_cleaned_201.csv")
print(_csv.columns)

"""
fragen: 

    1. wie viele spiele wurden vor 2015 gemacht -> release_date
    2. wie viele davon sind FSK 18 -> required_age
    3. sotiere nach menge DlC's absteigend dlc_count
    4. sotiere nach publishers und zeige die 5 zeilen an 
    5. was hat sie höchste average_playtime_2weeks

"""


# 1. 
_csv["release_date"] = pd.to_datetime(_csv["release_date"], errors="coerce")

vor_2015 = _csv[_csv["release_date"]<"2015-01-01"]
print(f" 1. Die anzahl der spiele sind {len(vor_2015)}")
print(vor_2015[["name","release_date"]].head(5))
print("")



# 2.
vor_2015_und_FSK_18 = _csv[(_csv["release_date"]<"2015-01-01") & (_csv["required_age"]>16)]
print(f" 1. Die anzahl der spiele die FSK 16 sind {len(vor_2015_und_FSK_18)}")
print(vor_2015_und_FSK_18)
print("")


# 3.
sorted_csv = _csv.sort_values("dlc_count", ascending=False)
print("Eine sortierte liste bezgen auf dlc's")
print(sorted_csv[["name", "dlc_count"]].head(10))
print("")


# 4.
grupp_pub = _csv.groupby("publishers")["name"].count()
grupp_pub = grupp_pub.sort_values(ascending=False)
print(grupp_pub.head(10))
print("")


# 5. was hat sie höchste average_playtime_2weeks.
print("was ist die höchst playtime in den letzten 2 wochen")
playtime_2w = _csv.sort_values("average_playtime_2weeks", ascending=False)
print(playtime_2w[["name","average_playtime_2weeks"]].head(10))