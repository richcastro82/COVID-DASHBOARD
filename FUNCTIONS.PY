# RICHARD CASTRO
# THE ACHESON GROUP - COVID DASHBOARD
# AUGUST 29TH, 2020 - FIRST CODE
# OCTOBER 02, 2020 - REVISED CODE
# DECEMBER 23RD, 2020 - FINAL CODING CRUNCH BEFORE LAUNCH

# IMPORTING MY LIBRARIES
from LIBRARIES import *

#SETTING THE GLOBAL VARIABLES USED FOR THE INITIAL LOADOUT

# V1 - This version has been renovated to V2 #
#----------------------------------------------------------------
#USED THIS HARD CODED CLIENT LIST ON V1 BUT MOVED INTO A VARIBLE SYSTEM.
#client_list = ['Pepsi', 'Kelloggs']
#Metrics_List = ['CASES', 'DEATHS', 'ACTIVE', 'RT', 'CR', 'MOB', 'TPR']
#location_types=['plant', 'facilities', 'processing', 'administrative']
#----------------------------------------------------------------

#CLIENT LOOKUP SYSTEM V2 SEARCHES A CLIENT DIRECTORY TO POPULATE THE CLIENT LIST
Directory=pd.read_csv('data/client_locations/client_seeding.csv')
Client_List=[]
Metrics_List=[]
Location_List=[]
Chart_List=[]

for i in Directory.clients:
    Client_List.append('{}'.format(i))

for i in Directory.metrics:
    Metrics_List.append('{}'.format(i))

for i in Directory.locations:
    Location_List.append('{}'.format(i))

for i in Directory.charts:
    Chart_List.append('{}'.format(i))




#-----------------------------------------------------------------------------
# CLIENT LOOKUP V3 WILL SEARCH CLIENT FOLDER FOR FILE NAMES AND POPULATE THE CLIENT
# LIST BASED ON THE FILES IN THE FOLDER
#
#-- NEEDS CODING FOR V3 UPDATES
#--------------------------------------------------------------------------------------------








#-----------------------------------------------------------------------------------------------
#
#-----------------------------------------------------------------------------------------------

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
mapbox_access_token = "pk.eyJ1Ijoia2luZ2Nhc3RybzgyIiwiYSI6ImNrZWQ5MjduNTBmNG8ycHM0YjV4NnM5ejEifQ.1GWNK066IM01BBQ-9vDluw"





################################################################################
#PATH = pathlib.Path(__file__).parent
#DATA_PATH = PATH.joinpath("DATA/Client_Locations/").resolve()
#df_PEPSI = pd.read_csv(DATA_PATH.joinpath("pepsi.csv"))
#df_KELLOGGS = pd.read_csv(DATA_PATH.joinpath("KELLOGGS.csv"))
#df_AW = pd.read_csv(DATA_PATH.joinpath("A&W.csv"))


#df1 = pd.read_csv('data/client_locations/kelloggs.csv')
#def make_client_table(df1):
#    """ Return a dash definition of an HTML table for a Pandas dataframe """
#    table = []
#    for row in df1.iterrows():
#        html_row = []
#        for i in range(len(row)):
#            #html_row.append(html.Td([row[i]]))
#            table.append(html.Tr(html_row))
#    return table

# THIS IS THE TOP HEADER SECTION: THIS SECTION WILL BE USED TO BRAND THE PAGE FOR THE CLIENT
# CLIENT LOGO AND NAME WILL CHANGE IN THIS SECTION DEPENDING ON THE CLIENT
################################################################################















#-----------------------------------------------------------------------------------------------
# Defining funcitons of the application
#-----------------------------------------------------------------------------------------------
# def building_cards():
#     card = dbc.Card(
#     [
#         dbc.CardImg(src="/IMAGES/dash-panel.png", top=True),
#         dbc.CardBody(
#             [
#                 html.H4("Card title", className="card-title"),
#                 html.P(
#                     "Some quick example text to build on the card title and "
#                     "make up the bulk of the card's content.",
#                     className="card-text",
#                 ),
#                 dbc.Button("Go somewhere", color="primary"),
#             ]
#         ),
#     ],
#     style={"width": "18rem"},
#     )
#     return card


def build_custom_g():
    return html.Div(
        id='',
        className='',
        children=[
            html.H2('')
        ]
    )


Client_Select=Client_List[1]



def build_branding():
    return html.Div(
        id='brandingHeader',
        className='brandingHeaderStyle',
        children=[
            html.Div(
            className='branding-left',
            children=[
                html.H2('logo goes here for {}'.format(Client_Select)),
                html.H2('Matrix Dashboard for {}'.format(Client_Select))
                ]
            ),
            html.Div(
                className='client_deets',
                children=[
                    html.P('Total Employees Tested: {}'.format(Chart_List[1]))]),
                    html.Div(
                    className='client_deets',
                    children=[
                        html.P('Total Employees Negative: {}'.format(Chart_List[1]))]),
                        html.Div(
                        className='client_deets',
                        children=[html.P('Total Employees Positive: {}'.format(Chart_List[1]))]),
                    html.Div(
                        className='client_deets',
                        children=[
                            html.P('Total Employees Culmaliative: {}'.format(Chart_List[1]))]),
        ]
    )




# GAUGE SECTION - THIS IS THE SECTION THAT SHOWS THE CURRENT COVID STATS FOR THE NATION
def build_gauges():
    return html.Div(
        id='header-header',
        className='header-header-class',
        children=[
            html.Div(
                id='header-box-1',
                children=[

#                    html.H3('{}'.format(df.score[1])),

                    html.Div(

                    id='daily-box-1',
                    className='StyledDataCard',
                    children=[
                    df.iloc[0]['score'],
                    html.A([df.iloc[0]['score']]),
                    html.P('Case Rate')
                    ]),

                    html.Div(
                    id='daily-box-2',
                    className='StyledDataCard',
                    children=[df.iloc[1]['score'], html.A([df.iloc[0]['score']]), html.P('RT')]),
                    html.Div(
                    id='daily-box-3',
                    className='StyledDataCard',
                    children=[df.iloc[2]['score'], html.A([df.iloc[0]['score']]), html.P('TPR')]),
                    html.Div(
                    id='daily-box-4',
                    className='StyledDataCard',
                    children=[df.iloc[3]['score'], html.A([df.iloc[0]['score']]), html.P('Mobility')]),
                    ])])





# THIS IS THE USER INPUT SECTION - THIS IS WHERE IS USER CAN SELECT FROM A
# LIST OF OPTIONS FOR SORTING AND FILTERING CHART DATA
def build_upper_left_panel():
    return html.Div(
    #LEFT-HEADER
    id="upper-left",
    className="six columns",
    children=[
        #LEFT-HEADER-TITLE
        dbc.Card([
        html.H2(
            className="section-title",
            children="Choose Location Data",
        ),

        html.Div(
            className="control-row-1",
            children=[
                html.Div(
                    id="state-select-outer",
                    children=[
                        html.H4("SELECT A LOCATION FILE"),
                        dcc.Dropdown(
                            id="Client_Select",
                            options=[{"label": i, "value": i} for i in Client_List],
                            value=Client_List[1],
                        ),
                    ],
                ),
                    html.Div(
                        id="dateSelect",
                        children=[
                            #DATE RANGE
                            dcc.DatePickerRange(
                                id='my-date-picker-range',
                                min_date_allowed=date(2020, 4, 15),
                                max_date_allowed=date(2020, 12, 31),
                                initial_visible_month=date(2020, 12, 15),
                                start_date=date(2020,12,1),
                                end_date=date(2020,12,25)
                                ),
                        ]),
                         html.Div(
                             id="region-select-outer-right",
                             className="control-row-2",
                             children=[
                                # html.Label("Filter Facility Locations"),
                            #     html.Div(
                            #         id="location_select-div",
                            #         children=dcc.Checklist(
                            #             id="location_select",
                            #             options=[{"label":i, "value": i} for i in Location_List],
                        #                 value=[Location_List[0]],
                        #             ),
                        #         ),
                             ],
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


],)])],)


# THIS IS THE METRIC SELECTION BOX
def build_upper_right_panel():
    return html.Div(
        #LEFT-HEADER
        id="upper-right",
        className="six columns",
        children=[
            #LEFT-HEADER-TITLE
            html.H2(
                className="section-title-right",
                children="Choose Chart Type",
            ),

            html.Div(
                className="control-row-1",
                children=[
                    html.Div(
                        id="state-select-outer-right",
                        children=[

                            html.H4("SELECT A FACILITY TYPE"),
                            dcc.Dropdown(
                                id="location_select", searchable=True,
                                options=[{"label": i, "value": i} for i in Location_List],
                                value=Location_List[0]
                            ),
                            html.H4("SELECT A METRIC"),
                            dcc.Dropdown(
                                id="metric_select", searchable=True,
                                options=[{"label": i, "value": i} for i in Metrics_List],
                                value=Metrics_List[0]
                            ),
                            html.H4("CHART TYPE"),
                            dcc.Dropdown(
                                id="chart-select", searchable=True,
                                options=[{"label": i, "value": i} for i in Chart_List],
                                value=Chart_List[3]
                            ),


                        ],
                    ),
                ],
            ),

        ],
    )



#=========================================================================================
# THIS SECTION IS FOR THE TABLE THAT DISPLAYS TO DATA UNDER THE CHART
# READ IN A CLIENT LOCATION FILE BASED ON THE USER INPUT
#Client_Select=Client_List[1]
#Client_File=pd.read_csv('data/client_locations/{}.csv'.format(Client_Select.value))
#df=Client_File.drop(['fips', 'country', 'lat', 'long'], axis=1)


tableCall=()
df = pd.read_csv('data/client_locations/{}.csv'.format(Client_List[0]))
df1=df
df1.drop(['fips', 'country', 'lat', 'long'], axis=1, inplace=True)
#==========================================================================================














#-----------------------------------------------------------------------------------------------
#   THE LAYOUT SECTION
#-----------------------------------------------------------------------------------------------

#==================================================================
#========== HTML & CSS CODE ====================================
#==========================================================
app.layout = html.Div(
    className="container scalable",
    children=[
            # CLIENT BRANDING ON THE HTML
            # DAILY GUAGES ON THE HTML
            #USER INPUT SECTIOIN - HTML SIDE
            html.Div(
                id="upper-container",className="row",
                    children=[
                        dbc.CardDeck([
                        build_upper_left_panel(),
                        build_branding(),
                        build_upper_right_panel(),])
                        #make_client_table(df1),
                    ],),

            build_gauges(),
            build_custom_g(),
#            building_cards(),


#OUTPUT HTML SECTION
            html.Div(
                id="show_data",
                className='twelve columns',
                children=[

#                html.Label('Timeline Slider'),
#                dcc.Slider(
#                    id='chartin',
#                    min=1,
#                    max=8,
#                    marks={i: 'Week {}'.format(i) for i in range(9)},
#                    value=4,
#                    ),

#                html.H2('Graphed Data'),

#OUTPUT SECTION - GRAPH
                dcc.Graph(id='Client_Output'),

#OUTPUT SECTION - TABLE
                dash_table.DataTable(
                    id='table',
                    columns=[{"name": i, "id": i} for i in df1.columns],
                    data=(df1.to_dict('records')),
        )
    ])
],)







#-----------------------------------------------------------------------------------------------
#   THE CALLBACK SECTION
#-----------------------------------------------------------------------------------------------

#*******************************************************************
@app.callback(
Output(component_id='tput', component_property='children'),
[Input(component_id='inpt', component_property='value')]
)
def update_t(input_data):
    return file
#*******************************************************************

#******************************************************************
@app.callback(
Output(component_id='Client_Output', component_property='figure'),
[Input(component_id='Client_Select', component_property='value'),
Input(component_id='location_select', component_property='value'),
Input(component_id='metric_select', component_property='value'),]
)

def buildchart(chart_data, loc_data, met_data):
    date_me="12/21/2020"
    file=pd.read_csv('DATA/Client_Locations/{}.csv'.format(chart_data))
    location=loc_data
    metric=met_data
    chart_data=chart_data
    #client_stuff=file[file['locations']=='{}'.format(location)]
    #client_stuff= client_stuff[client_stuff['metrics']=='{}'.format(metric)]

    figchart = px.scatter(
            #client_stuff,
            file,
            #min=1,#max=100,#range_y=[40,100],
            color="score",
            size="pop",
            hover_data=['county','state'],
            x='fips',
            y='score',
            title="TAG Dash for {} Facility Locations for {}".format(chart_data, date_me),
        )

    return figchart
#****************************************************************
# @app.callback(
# Output(component_id='', component_property=''),
# [Input(component_id='', component_property='')]
# )
