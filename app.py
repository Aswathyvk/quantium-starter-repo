import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load processed data
df = pd.read_csv("data/output.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

app = Dash(__name__)

COLORS = {
    "background": "#1e1e2f",
    "text": "#f2f2f2",
    "accent": "#ff6f91",
}

app.layout = html.Div(
    style={
        "backgroundColor": COLORS["background"],
        "color": COLORS["text"],
        "fontFamily": "Segoe UI, sans-serif",
        "padding": "40px",
        "minHeight": "100vh",
    },
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            style={"textAlign": "center", "color": COLORS["accent"]},
        ),
        html.Div(
            [
                html.Label("Select Region:", style={"fontSize": "18px"}),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                        {"label": "All", "value": "all"},
                    ],
                    value="all",
                    inline=True,
                    style={"marginTop": "10px"},
                    labelStyle={"marginRight": "20px"},
                ),
            ],
            style={"textAlign": "center", "marginBottom": "30px"},
        ),
        dcc.Graph(id="sales-chart"),
    ],
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value"),
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered = df
    else:
        filtered = df[df["Region"] == selected_region]

    daily_sales = filtered.groupby("Date", as_index=False)["Sales"].sum()

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales Over Time ({selected_region.capitalize()})",
        labels={"Date": "Date", "Sales": "Sales ($)"},
    )
    fig.update_layout(
        plot_bgcolor=COLORS["background"],
        paper_bgcolor=COLORS["background"],
        font_color=COLORS["text"],
    )
    fig.update_traces(line_color=COLORS["accent"])
    return fig


if __name__ == "__main__":
    app.run(debug=True)