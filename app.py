from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
df = pd.read_csv("formatted_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")
app = Dash(__name__)
app.title = "Pink Morsel Sales Dashboard"
app.layout = html.Div(

    style={
        "backgroundColor": "#F5F7FA",
        "padding": "30px",
        "fontFamily": "Arial, sans-serif"
    },

    children=[

        html.H1(
            "Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#1F3A5F",
                "fontSize": "48px",
                "fontWeight": "bold",
                "marginBottom": "10px"
            }
        ),

        html.P(
            "Interactive dashboard for analysing Pink Morsel sales over time.",
            style={
                "textAlign": "center",
                "fontSize": "22px",
                "color": "#666666",
                "marginBottom": "40px"
            }
        ),

        html.Div(

            children=[

                html.Label(
                    "Filter Sales by Region",
                    style={
                        "fontWeight": "bold",
                        "fontSize": "22px",
                        "display": "block",
                        "marginBottom": "15px"
                    }
                ),

                dcc.RadioItems(
                    id="region-picker",

                    options=[
                        {"label": " All", "value": "all"},
                        {"label": " North", "value": "north"},
                        {"label": " South", "value": "south"},
                        {"label": " East", "value": "east"},
                        {"label": " West", "value": "west"},
                    ],

                    value="all",

                    inline=True,

                    labelStyle={
                        "fontSize": "18px",
                        "marginRight": "30px"
                    }

                )

            ],

            style={
                "textAlign": "center",
                "marginBottom": "40px"
            }

        ),

            dcc.Graph(id="sales-graph")
    ]

)
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales Over Time",
        template="plotly_white"
    )

    fig.update_traces(
        line=dict(
            color="#E91E63",
            width=3
        )
    )

    fig.update_layout(

        title={
            "text": "Pink Morsel Sales Over Time",
            "x": 0.5,
            "xanchor": "center",
            "font": {
                "size": 30
            }
        },

        xaxis_title="Date",

        yaxis_title="Sales ($)",

        hovermode="x unified",

        font={
            "family": "Arial",
            "size": 16
        },

        margin=dict(
            l=60,
            r=40,
            t=80,
            b=60
        ),

        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF"
    )

    return fig
if __name__ == "__main__":
    app.run(debug=True)