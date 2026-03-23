import pandas as pd
import plotly.express as px

#  übung tag 71
# csv (games_march2025_cleaned_201.csv) einlesen
# playtime 2 weeks gegen all time -> balken diagramm

# line diagramm (
#  average_playtime_2weeks,
#  median_playtime_forever,
#  median_playtime_2weeks,
#  average_playtime_forever,
#  score_rank
#  )

_csv = pd.read_csv("games_march2025_cleaned_201.csv")

name = _csv["name"]
publishers = _csv["publishers"]
average_playtime_2weeks = _csv["average_playtime_2weeks"]
median_playtime_2weeks = _csv["median_playtime_2weeks"]
average_playtime_forever = _csv["average_playtime_forever"]
median_playtime_forever = _csv["median_playtime_forever"]


df = pd.DataFrame(
    {
        "name": name,
        "publishers": publishers,
        "average_playtime_2weeks": average_playtime_2weeks,
        "median_playtime_2weeks": median_playtime_2weeks,
        "average_playtime_forever": average_playtime_forever,
        "median_playtime_forever": median_playtime_forever,
    }
)

fig_line = px.line(
    df[:25],
    x="name",
    y=[
        "median_playtime_2weeks",
        "average_playtime_2weeks",
        "median_playtime_forever",
        "average_playtime_forever",
    ],
    title=" Playtime - Analyse ",
    markers=True,
)

fig_line.write_html("uebung_71.html")

fig_bar = px.bar(
    df[:25],
    x="name",
    y=[
        "median_playtime_2weeks",
        "average_playtime_2weeks",
        "median_playtime_forever",
        "average_playtime_forever",
    ],
    title=" Playtime - Analyse ",
)

fig_bar.update_layout(barmode="group")
fig_bar.write_html("uebung_71_bar.html")
