# RICHARD CASTRO
# THE ACHESON GROUP - COVID DASHBOARD
# AUGUST 29TH, 2020 - FIRST CODE
# OCTOBER 02, 2020 - REVISED CODE
# DECEMBER 23RD, 2020 - FINAL CODING CRUNCH BEFORE LAUNCH

#IMPORTING MY LIBRARIES
from LIBRARIES import *

#SETTING THE GLOBAL VARIABLES USED FOR THE INITIAL LOADOUT
#----------------------------------------------------------------
#USED THIS HARD CODED CLIENT LIST ON V1 BUT MOVED INTO A VARIBLE SYSTEM.
#client_list = ['Pepsi', 'Kelloggs']
#Metrics_List = ['CASES', 'DEATHS', 'ACTIVE', 'RT', 'CR', 'MOB', 'TPR']
#location_types=['plant', 'facilities', 'processing', 'administrative']
#----------------------------------------------------------------


#CLIENT LOOKUP SYSTEM V2 SEARCHES A CLIENT DIRECTORY TO POPULATE THE CLIENT LIST
Directory=pd.read_csv('data/client_locations/client_directory2.csv')
Client_List=[]
Metrics_List=[]
Location_Types=[]

for i in Directory.clients:
    Client_List.append('{}'.format(i))

for i in Directory.metrics:
    Metrics_List.append('{}'.format(i))

for i in Directory.locationTypes:
    Location_Types.append('{}'.format(i))

#-----------------------------------------------------------------------------

# CLIENT LOOKUP V3 WILL SEARCH CLIENT FOLDER FOR FILE NAMES AND POPULATE THE CLIENT
# LIST BASED ON THE FILES IN THE FOLDER
#
#-- NEEDS CODING FOR V3 UPDATES
#
#--------------------------------------------------------------------------------------------

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
def build_branding():
    return html.Div()


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
                    class='StyledDataCard',
                    children=[df.iloc[0]['score'], html.P('Case Rate'), html.A([df.iloc[0]['score']])]),
                    html.Div(
                    id='daily-box-2',
                    class='StyledDataCard',
                    children=[df.iloc[1]['score'], html.P('RT'), html.A([df.iloc[0]['score']])]),
                    html.Div(
                    id='daily-box-3',
                    class='StyledDataCard',
                    children=[df.iloc[2]['score'], html.P('TPR'), html.A([df.iloc[0]['score']])]),
                    html.Div(
                    id='daily-box-4',
                    class='StyledDataCard',
                    children=[df.iloc[3]['score'], html.P('Mobility'), html.A([df.iloc[0]['score']])]),
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
                            value=Client_List[0],
                        ),
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
),],)],)


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

                            html.H4("SELECT A METRIC"),
                            dcc.Dropdown(
                                id="clientin-right", multi=True, searchable=True,
                                options=[{"label": i, "value": i} for i in Metrics_List],
                                value=""
                            ),
                        ],
                    ),
                ],
            ),

             html.Div(
                 id="region-select-outer-right",
                 className="control-row-2",
                 children=[
                    # html.Label("Filter Facility Locations"),
                     html.Div(
                         id="checklist-container-right",
                         children=dcc.Checklist(
                             id="region-select-all-right",
                             options=[{"label":i, "value": i} for i in Locations_List],
                             value=[Locations_List[0]],
                         ),
                     ),
                 ],
             )
        ],
    )



#=========================================================================================
# THIS SECTION IS FOR THE TABLE THAT DISPLAYS TO DATA UNDER THE CHART
# READ IN A CLIENT LOCATION FILE BASED ON THE USER INPUT
Client_File=pd.read_csv('data/client_locations/{}.csv'.format(Client_Select.value))
df=Client_File.drop(['fips', 'country', 'lat', 'long'], axis=1)


#df = pd.read_csv('data/client_locations/kelloggs.csv')
#df1=df
#df1.drop(['fips', 'country', 'lat', 'long'], axis=1, inplace=True)
#==========================================================================================



#==================================================================
#========== HTML & CSS CODE ====================================
#==========================================================
app.layout = html.Div(
    className="container scalable",
    children=[
            # CLIENT BRANDING ON THE HTML
            html.Div(
            id='build-branding',children=[build_branding()]),
            # DAILY GUAGES ON THE HTML
            html.Div(
            id='build-guages',children=[build_guages()]),
            #USER INPUT SECTIOIN - HTML SIDE
            html.Div(
                id="upper-container",className="row",
                    children=[
                        #LOCATION DATA
                        build_upper_left_panel(),
                        #METRIC DATA
                        build_upper_right_panel(),
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
                        #make_client_table(df1),
                    ],
            ),







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
                    data=df1.to_dict('records'),
        )
    ])
],)






#**********************************************
#@app.callback(
#Output(component_id='tput', component_property='children'),
#[Input(component_id='inpt', component_property='value')]
#)
#def update_t(input_data):
#    return file

#************************************************

@app.callback(
Output(component_id='Client_Output', component_property='figure'),
[Input(component_id='Client_Select', component_property='value')]
)
def buildchart(chart_data):
    date_me="12/21/2020"
    #client_stuff=pd.read_csv('data/clients/kelloggs12.csv')
    file=pd.read_csv('DATA/Client_Locations/{}.csv'.format(chart_data))
    client_stuff=file
    #file = pd.read_csv('data/clients/kelloggs12.csv')
    #client_stuff=file[file['date']=='12/21/2020']
    #client_stuff=file[file['fips']== 1005]

    #client_stuff=client_stuff.sort_values(by=['score'], ascending=False)

    #client_stuff=client_stuff.head(15)

    figchart = px.scatter(
        client_stuff,
        #min=1,
        #max=100,
        color="score",
        size="pop",
        hover_data=['county','state'],
        x='county',
        y='employeeCount',
        title="TAG Dash for {} Facility Locations for {}".format(chart_data, date_me),
        #range_y=[40,100],
        )

    return figchart
