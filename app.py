import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
df = pd.read_csv("formatted_sales.csv")
df["Date"] = pd.to_datetime(df["Date"])
daily_sales = (
    df.groupby("Date")["Sales"]
      .sum()
      .reset_index()
)
fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales by Date",
    markers=False
)

fig.update_layout(
    template="plotly_white",

    title={
        "text": "Pink Morsel Sales by Date",
        "x":0.5,
        "font":{"size":26}
    },

    xaxis_title="Date",
    yaxis_title="Sales ($)",

    hovermode="x unified",

    font=dict(size=15),

    margin=dict(
        l=40,
        r=40,
        t=70,
        b=40
    )
)

fig.update_traces(
    line=dict(
        width=3,
        color="#E91E63"
    )
)

app = Dash(__name__)

app.layout = html.Div(

    children=[

        html.H1(
            "Pink Morsel Sales Visualisation",
            style={
                "textAlign":"center",
                "marginBottom":"10px"
            }
        ),

        html.P(
            "Sales data for Pink Morsels over time.",
            style={
                "textAlign":"center",
                "fontSize":"18px",
                "color":"gray",
                "marginBottom":"25px"
            }
        ),

        dcc.Graph(
            figure=fig
        )

    ],

    style={
        "width":"90%",
        "margin":"auto",
        "padding":"30px"
    }

)

if __name__ == "__main__":
    app.run(debug=True)