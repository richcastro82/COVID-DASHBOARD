# RICHARD CASTRO
from LIBRARIES import *
app = dash.Dash(__name__, )

#************************************************************************************************
# THIS IS THE OBJECT CLASS CARD TYPE FOR THE CLIENT SCORE CARDS // COVID CUSTOM DASHBOARD SECTION
#************************************************************************************************
def tag_score_card(dfs, df):
    tagCard = dbc.Card([
        dbc.CardBody([
            html.Div(id='tag-card-id', className='tag-score-card', children=[
                html.Div( id="card-top", className='tag-card', children=[html.H3("{}".format(dfs))]),
                html.Div( id="card-left",  className='tag-card', children=[html.H4("{}".format(df.state)),html.H4("{}".format(df.county))]),
                html.Div( id="card-center", className='tag-card',  children=[html.H2("{}".format(df.score))]),
                html.Div( id="card-right", className='tag-card',  children=[html.H4("{}".format(df.employeeCount)),html.H4("{}".format(df.fips))]),
                html.Div( id="card-bottom", className='tag-card',  children=[html.H3("{}".format(df.county))]),
            ])]),],)
    return tagCard

#***********************************************
# THIS IS THE LAYOUT SECTION OF THE APPLICATION
#***********************************************
app.layout = html.Div(
    className="container scalable",
    children=[
        html.Div(
        className="client-tile",
            children=[
                dcc.Dropdown(id='tagselect', options=[{'label':'kelloggs', 'value':'kelloggs'},{'label':'pepsi', 'value': 'pepsi'}],value='kelloggs'),
                dbc.CardDeck(id='tagtiles'),
])])

#*********************************************
# THIS IS CALLBACK SECTION OF THE APPLICATION
#*********************************************
@app.callback(Output('tagtiles', 'children'),
[Input('tagselect', 'value')])

def tagtileUpdate(clientDeets):
    dfs=clientDeets
    ret=[]
    df=pd.read_csv('data/client_locations/{}.csv'.format(dfs))
    for i, row in df.iterrows():
        ret.append(tag_score_card(dfs, row))
    return dbc.CardDeck(ret)

if __name__ == '__main__':
    app.run_server(debug=True)
