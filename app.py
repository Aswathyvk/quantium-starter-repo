import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load processed data
df = pd.read_csv("data/output.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Aggregate sales by date (sum across regions)
daily_sales = df.groupby("Date", as_index=False)["Sales"].sum()

fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={"Date": "Date", "Sales": "Sales ($)"},
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)