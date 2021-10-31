# RICHARD CASTRO
# DASHBOARD APP TEMPLATE FILE
# this is the barebones framework for the dashboard app


from LIBRARIES import *



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE])


app.layout = html.Div(

children=[

dbc.CardDeck([
dbc.Card(
    [
        dbc.CardImg(src="images/pro1.png", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],),
dbc.Card(
    [
        dbc.CardImg(src="../IMAGES/pro2.png", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],),
dbc.Card(
    [
        dbc.CardImg(src="images/pro3.png", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],),
    dbc.Card(
        [
            dbc.CardImg(src="images/pro4.png", top=True),
            dbc.CardBody(
                [
                    html.H4("Card title", className="card-title"),
                    html.P(
                        "Some quick example text to build on the card title and "
                        "make up the bulk of the card's content.",
                        className="card-text",
                    ),
                    dbc.Button("Go somewhere", color="primary"),
                ]
            ),
        ],),

])


])




if __name__ == '__main__':
    app.run_server(debug=True)
