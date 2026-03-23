import pandas as pd
import plotly.express as px

# Daten vorbereiten

years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
sales = [50, 60, 55, 80, 90, 70, 100, 110, 105, 130]
costs = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]

df = pd.DataFrame(
    {
        "year": years,
        "sales": sales,
        "costs": costs,
    }
)


# Plot erstellen (line-Diagramm)

fig = px.line(
    df,
    x="year",
    y="sales",
    title="Verkäufe pro Jahr",
    markers=True,
)

fig.write_html("plot.html")


# Balnkendiagramm

fig_bar = px.bar(df, x="year", y="sales", title="Verkäufe pro Jahr (Balkendiagramm)")

fig_bar.write_html("plot_bar.html")


# Balnkendiagramm mit 2 vergleichswerten

fig_bar_with_two = px.bar(
    df, x="year", y=["sales", "costs"], title="Verkäufe pro Jahr (Balkendiagramm)"
)

fig_bar_with_two.update_layout(barmode="group")
fig_bar_with_two.write_html("plot_bar_with_two.html")


# Line-Diagramm mit 2 Linien

fig_two_lines = px.line(
    df,
    x="year",
    y=["sales", "costs"],
    title="Verkäufe pro Jahr",
    markers=True,
)

fig_two_lines.write_html("plot_sales_costs.html")
