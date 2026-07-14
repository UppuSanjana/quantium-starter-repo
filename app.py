from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("formatted_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Dashboard"),

    dcc.RadioItems(
        id="region-picker",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "South", "value": "south"},
            {"label": "East", "value": "east"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True,
    ),

    dcc.Graph(id="sales-graph")
])


@app.callback(
    Output("sales-graph", "figure"),
    Input("region-picker", "value"),
)
def update_graph(region):

    if region == "all":
        dff = df
    else:
        dff = df[df["Region"].str.lower() == region]

    fig = px.line(
        dff,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales Over Time"
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)