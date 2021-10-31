# RICHARD CASTRO
# DASHBOARD APP TEMPLATE FILE
# this is the barebones framework for the dashboard app


from LIBRARIES import *
import plotly.express as px
import plotly.graph_objs as go
import plotly.graph_objects as goo
import numpy as np
#external_stylesheets = ['']

def build_test():
    df=pd.read_csv('data/client_locations/pepsi.csv')
    figchart = px.scatter(
            df,
            #min=1,#max=100,#range_y=[40,100],
            color="score",
            size="pop",
            hover_data=['county','state'],
            x='fips',
            y='score',
            title="TAG",
        )

    return figchart






#CLIENT LOOKUP SYSTEM V2 SEARCHES A CLIENT DIRECTORY TO POPULATE THE CLIENT LIST

Metrics=['Mobility', 'Case_Rate', 'Rate_Transmission', 'Test_Rate']
Chart_List=['Map', 'Bar', 'Line', 'Scatter']
state_list=['florida', 'california']


def build_modal():
        modal = html.Div(
            [
                dbc.Button("Download reports", id="open"),
                dbc.Modal(
                    [
                        dbc.ModalHeader("These are the previous weekly matrix reports"),
                        dbc.ModalBody(id='popbody', children=[
                        html.Ul([
                        html.Li(html.A(href='#',children=('November 23'))),
                        html.Li(html.A(href='#',children=('November 29'))),
                        html.Li(html.A(href='#',children=('December 7'))),
                        html.Li(html.A(href='#',children=('December 16'))),
                        html.Li(html.A(href='#',children=('December 22'))),
                        html.Li(html.A(href='#',children=('December 28'))),
                        html.H4('Need to go further back? Contact our team so we can make that happen'),
                        html.A(href='support@achesongroup.com',children=('email us'))
                        ])]),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="close", className="ml-auto")
                        ),
                    ],
                    id="modal",
                ),
            ]
        )
        return modal


#df1.drop(['fips', 'country', 'lat', 'long'], axis=1, inplace=True)



# THIS IS THE USER INPUT SECTION - THIS IS WHERE IS USER CAN SELECT FROM A
# LIST OF OPTIONS FOR SORTING AND FILTERING CHART DATA
def build_upper_left_panel():
    return html.Div(
    #LEFT-HEADER

    children=[
        #LEFT-HEADER-TITLE
                    html.H4("SELECT A METRIC"),
                    dcc.Dropdown(
                        id="metric_select",
                        options=[{"label": i, "value": i} for i in Metrics],
                        value=Metrics[0],
                    ),

                    html.H4("FILTER BY STATE"),
                    dcc.Dropdown(
                        id="state_select",
                        options=[{"label": i, "value": i} for i in state_list],
                        value=state_list[0],
                    ),

                dcc.Upload(
                   id='upload-data',
                   children=html.Div([
                       'Drag and Drop or ',
                       html.A('Select Files')
                       ]),
                       style={
                       'width': '100%',
                       'height': '60px',
                       'lineHeight': '60px',
                       'borderWidth': '1px',
                       'borderStyle': 'dashed',
                       'borderRadius': '5px',
                       'textAlign': 'center',
                       'margin-top':'30px'
                       },
                       # Allow multiple files to be uploaded
                       multiple=True
                       ),
                       build_modal()
])







pd.options.display.float_format = '{:,}'.format

df=pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv')
tc=df['cases'][348]-df['cases'][347]
td=df['deaths'][348]-df['deaths'][347]
dftt=df
dff=df
dftt['cases']=dftt.apply(lambda x: "{:,}".format(x['cases']), axis=1)
dftt['deaths']=dftt.apply(lambda x: "{:,}".format(x['deaths']), axis=1)
dfdfdf=dftt['cases'][df['date']=='2020-12-28']
dfdfdf=dfdfdf.to_dict()

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

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.SANDSTONE])


app.layout = html.Div(
    id='main-container',
    className='twelve columns',
    children=[



        html.Div(
        id='topper',
        className='appheader',
        children=[
        html.Div(
            id='topperInner',
            children=[
                html.Img(className='topperImage', src='assets/logo.png'),
                html.H2('COVID Dashboard - Weekly Matrix Reports'),
                html.P('The Acheson Group'),
                ])
        ]),



html.Div(id='inner-container', children=[
        dbc.CardDeck(
            className='row',
            children=[
            dbc.Card([
            dbc.CardHeader(children=[html.H4(className='Fl',children=['Filter']),html.H4(className='FlH',children=['Results'])]),
                dbc.CardBody(
                    [
                    build_upper_left_panel()

                    ]
                ),
                ],

            ),
                dbc.Card([
                dbc.CardHeader(children=[html.H4(className='Fl',children=['National']),html.H4(className='FlH',children=['Cases'])]),
                    dbc.CardBody(
                        [
                            html.H4("{}".format(dftt['cases'][348]), className="card-title"),
                            html.P("+{} since yesterday".format(tc), className="card-text"),
                        ]
                    ),dbc.CardFooter(className='tagf',children=[])
                    ],

                ),

                dbc.Card([
                dbc.CardHeader(children=[html.H4(className='Fl',children=['National']),html.H4(className='FlH',children=['Deaths'])]),
                    dbc.CardBody(
                        [
                            html.H4("{}".format(dftt['deaths'][348]), className="card-title"),
                            html.P("+{} since yesterday".format(td), className="card-text"),
                        ]
                    ),dbc.CardFooter(className='tagf',children=[])
                    ],

                ),



            dbc.Card([
            dbc.CardHeader(children=[html.H4(className='Fl',children=['National']),html.H4(className='FlH',children=['Recovery'])]),
                dbc.CardBody(
                    [
                        html.H4("{}".format(TAGcases[348]), className="card-title"),
                        html.P("{}".format(TAGcases[80]), className="card-text"),
                    ]
                ),dbc.CardFooter(className='tagf',children=[])
                ],

            ),
            ]
        ),
        dbc.CardDeck(
            className='row',
            children=[

    dbc.Card(id='tagChart1',children=[
    dbc.CardHeader(children=[

        #html.H2(className='ttt',children=['Updated: ']),
        #html.H2(className='FlH',children=['Graph']),
        html.H2(id='chartname',children=['']),]),
        dbc.CardBody(
            [
            html.P(id='stateChartPara', children=['The case rate per 100,000 people is the normalized number of confirmed cases per 100,000 people in a population. Case rate information is useful for identifying trends over a 2 – 4-week period. This information allows for relative risk comparisons to be made among regions and plants. This analysis calculates a 7-day rolling average of the number of cases per 100,000 people in the regions. A case rate >25 would indicate that an outbreak is uncontrolled and strict measures be undertaken to ensure safety of site and/or people (highlighted in red with red text).']),
            html.Div(id='out', children=[''])

            ]
        ),
        dbc.CardFooter(
        className='tagf', children=[html.H4(className='left', children=['Your brand protection is our highest priority']), html.H4(className='right', children=['www.AchesonGroup.com'])]
        )
    ],),

    dbc.Card(id='tagChart2',children=[
    dbc.CardHeader(children=[
        html.Img(src='assets/logo.png', className='topperImage'),
        #html.H2(className='ttt',children=['Updated: ']),
        #html.H2(className='FlH',children=['Graph']),
        html.H2(id='chartname2',className='ttt',children=['']),]),
        dbc.CardBody(
            [
            html.P(id='stateChartPara2', children=['']),
            html.Div(id='out2', children=['']),


            ]
        ),
        dbc.CardFooter(
        className='tagf', children=[html.H4(className='left', children=['Your brand protection is our highest priority']), html.H4(className='right', children=['www.AchesonGroup.com'])]
        )
    ],),

            ]
        ),
        dbc.CardDeck(
            className='row',
            children=[

    dbc.Card([
    dbc.CardHeader(children=[html.H4(className='Fl',children=['Weekly']),html.H4(className='FlH',children=['Report'])]),
        dbc.CardBody(
            [




            ]
        ),
        ],

    ),

            ]
        ),
    ]

)
])


datein='August 13, 2021'
@app.callback(
Output(component_id='chartname', component_property='children'),
[Input(component_id='metric_select', component_property='value')]
)
def build_name(metric):
    return html.H2('{} report for: General'.format(metric))


@app.callback(
Output(component_id='out', component_property='children'),
[Input(component_id='metric_select', component_property='value')]
)

def build_outputsection(chart_data):
        df = pd.read_csv('data/sources/{}.csv'.format(chart_data))
        df1=df
        return html.Div(
                id="show_data",
                className='twelve columns',
                children=[
                dash_table.DataTable(
                    id='table',
                    editable=True,
                    export_format='xlsx',
                    export_headers='display',
                    merge_duplicate_headers=True,
                    style_cell={'textAlign': 'right'},
                    style_data_conditional=[
                        {
                            'if': {'row_index': 'odd'},
                            'backgroundColor': 'rgb(248, 248, 248)'
                        },

                         {
                            'if': {
                                'filter_query': '{12/8/2020} > 0 && {12/8/2020} < .06',
                                'column_id': 'State'
                            },
                            'backgroundColor': '#6c877f',
                            'color': 'white'
                        },
                         {
                            'if': {
                                'filter_query': '{12/8/2020} > .06 && {12/8/2020} < .07',
                                'column_id': 'State'
                            },
                            'backgroundColor': '#fcb100',
                            'color': 'white'
                        },
                         {
                            'if': {
                                'filter_query': '{12/8/2020} > .07 && {12/8/2020} < .2',
                                'column_id': 'State'
                            },
                            'backgroundColor': '#973333',
                            'color': 'white'
                        },
                        {
                            'if': {
                                'filter_query': '{{12/8/2020}} = {}'.format(df1['12/8/2020'].max()),
                                'column_id': '12/8/2020'
                            },
                            'backgroundColor': '#973333',
                            'color': 'white'
                        },
                        {
                            'if': {
                                'filter_query': '{{12/15/2020}} = {}'.format(df1['12/15/2020'].max()),
                                'column_id': '12/15/2020'
                            },
                            'backgroundColor': '#973333',
                            'color': 'white'
                        },
                        {
                            'if': {
                                'filter_query': '{{12/22/2020}} = {}'.format(df1['12/22/2020'].max()),
                                'column_id': '12/22/2020'
                            },
                            'backgroundColor': '#973333',
                            'color': 'white'
                        },
                        {
                            'if': {
                                'filter_query': '{{12/8/2020}} = {}'.format(df1['12/8/2020'].min()),
                                'column_id': '12/8/2020'
                            },
                            'backgroundColor': '#fcb100',
                            'color': 'white'
                        },
                        {
                            'if': {
                                'filter_query': '{{12/15/2020}} = {}'.format(df1['12/15/2020'].min()),
                                'column_id': '12/15/2020'
                            },
                            'backgroundColor': '#fcb100',
                            'color': 'white'
                        },
                        {
                            'if': {
                                'filter_query': '{{12/22/2020}} = {}'.format(df1['12/22/2020'].min()),
                                'column_id': '12/22/2020'
                            },
                            'backgroundColor': '#fcb100',
                            'color': 'white'
                        },

                    ],

                    style_cell_conditional=[
                        {
                            'if': {'column_id': 'State'},
                            'textAlign': 'center'
                        }
                    ],
                    columns=[{"name": i, "id": i} for i in df1.columns],
                    data=(df1.to_dict('records')),
)])



@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open







if __name__ == '__main__':
    #app.run_server(host='0.0.0.0', ssl_context=('5ff832a347c541dd.pem', 'myserver.key'))
    app.run_server(host="0.0.0.0", port=443, ssl_context=('cert.pem', 'key.pem'))
