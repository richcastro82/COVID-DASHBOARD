from LIBRARIES import *


app = dash.Dash(
        __name__,

        meta_tags=[
            {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no",
            }],)


#SETTING UP THE APP SERVER FLASK AND API KEY FOR MAPBOX
server = app.server
app.config["suppress_callback_exceptions"] = True



#************************************************************************************************************
# THIS IS THE OBJECT CLASS CARD TYPE FOR THE COVID DASHBOARD PAGE TOP BANNER // COVID OPEN DASHBOARD SECTION
#************************************************************************************************************
def dash_top_banner():
    topperCard=dbc.Card([
    dbc.CardBody([
    html.H4('Fort Myers, FL'),
    html.H4('Case Rate: 45%'),
    html.P('Dashboard - Login'),
    ])
    ],className='topper',)
    return topperCard
#******************************************************************************************************
#******************************************************************************************************


#**********************************************************************************************
# THIS IS THE OBJECT CLASS CARD TYPE FOR THE CLIENT SCORE CARDS // COVID CUSTOM DASHBOARD SECTION
#**********************************************************************************************
def tag_score_card(deets, df):

    tagCard = dbc.Card([
        dbc.CardBody(
            [
            html.Div(id='tag-card-id', className='tag-score-card', children=[
                html.Div( id="card-top", className='tag-card', children=[html.H3("{}".format(deets))]),
                html.Div( id="card-left",  className='tag-card', children=[html.H4("{}".format(df.state)),html.H4("{}".format(df.county))]),
                html.Div( id="card-center", className='tag-card',  children=[html.H2("{}".format(df.score))]),
                html.Div( id="card-right", className='tag-card',  children=[html.H4("{}".format(df.employeeCount)),html.H4("{}".format(df.fips))]),
                html.Div( id="card-bottom", className='tag-card',  children=[html.H3("{}".format(df.county))]),
                ])]),],
    )
    print(tagCard)
    return tagCard


#**********************************************************************************
#**********************************************************************************







#*****************************************************************************************************
# THIS IS THE OBJECT CLASS CARD TYPE FOR THE COVID DASHBOARD MAIN PAGE // COVID OPEN DASHBOARD SECTION
#*****************************************************************************************************
def dash_main_cards(dfg, dff, dfff):
    mainCards= dbc.Card([
    dbc.CardHeader("TAG Score Card"),
        dbc.CardBody(
            [
                html.H4("{}".format(dfg), className="card-title"),
                html.P("{}".format(dff), className="card-text"),
            ]
        ),
        dbc.CardFooter(dfff)],
        style={"width": "18rem"}
    )

    return mainCards
#**********************************************************************************************
#**********************************************************************************************
userinput='kelloggs'
df=pd.read_csv('data/client_locations/kelloggs.csv')
#tagRT=(df.rt)
#tagCR=(df.cr)
#tagScore=(df.score)
#tagMOB=(df.mob)






df=pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv')
dff=df[df['date']=='2021-01-01']
dfc=dff.to_dict()
dfcc=dfc['cases']
TAGcases=list(dfcc.values())
dfCR=dfc['deaths']
TAGdeaths=list(dfCR.values())
print(dfc)


cdf=pd.read_csv('data/data.csv')
cdfa=cdf.to_dict('data')
print(cdf)
print(cdfa)






#==================================================================
#========== HTML & CSS CODE ====================================
#==========================================================
app.layout = html.Div(
    className="container scalable",
    children=[

            html.Div(
            id='topper',
            className='appheader',
            children=[
            html.Div(
                id='topperInner',
                children=[
                    html.Img(className='topperImage', src='assets/logo.png'),
                    html.H2('COVID Dashboard - TAG Scorecard for {}'.format('client name')),
                    html.P('The Acheson Group'),
                    ])
            ]),









        html.Div(
        className="tagScoreBody",
        children=[
            dcc.Dropdown(id='tagselect', options=[{'label':'Example', 'value':'TAG-Example'},{'label':'kelloggs', 'value':'kelloggs'},{'label':'pepsi', 'value': 'pepsi'}],value='kelloggs'),
            dbc.CardGroup(id='tagtiles'),
        ])
])



@app.callback(Output('tagtiles', 'children'),
[Input('tagselect', 'value')])

def tagtileUpdate(clientDeets):
    dfs=clientDeets
    ret=[]
    df=pd.read_csv('data/client_locations/{}.csv'.format(dfs))
    for i, row in df.iterrows():
        ret.append(tag_score_card(dfs, row))
    return dbc.CardGroup(ret)
