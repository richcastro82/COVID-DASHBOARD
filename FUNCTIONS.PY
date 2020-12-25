from LIBRARIES import *
import plotly.graph_objects as go
import dash_table


client_list = ['1', 'CA', 'fl', 'US FOODS']
metric_list = ['CASES', 'DEATHS', 'ACTIVE', 'RT', 'CR', 'MOB', 'TPR']
location_types=['plant', 'facilities', 'processing', 'administrative']



app = dash.Dash(
        __name__,
        meta_tags=[{
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no",
            }],
)



server = app.server
app.config["suppress_callback_exceptions"] = True
mapbox_access_token = "pk.eyJ1Ijoia2luZ2Nhc3RybzgyIiwiYSI6ImNrZWQ5MjduNTBmNG8ycHM0YjV4NnM5ejEifQ.1GWNK066IM01BBQ-9vDluw"




PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("DATA/clients/").resolve()
df_PEPSI = pd.read_csv(DATA_PATH.joinpath("client2.csv"))
df_KELLOGGS = pd.read_csv(DATA_PATH.joinpath("KELLOGGS.csv"))
#df_AW = pd.read_csv(DATA_PATH.joinpath("A&W.csv"))









def make_client_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table






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
                            options=[{"label": i, "value": i} for i in client_list],
                            value=client_list[0],
                        ),
                    ],
                ),
            ],
        ),

         html.Div(
             id="region-select-outer",
             className="control-row-2",
             children=[
                # html.Label("Filter Facility Locations"),
                 html.Div(
                     id="checklist-container",
                     children=dcc.Checklist(
                         id="region-select-all",
                         options=[{"label":i, "value": i} for i in location_types],
                         value=[],
                     ),
                 ),
             ],
         )
    ],

    )







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
                        id="state-select-outer",
                        children=[
                            html.Label("SELECT A CLIENT"),
                            dcc.Dropdown(
                                id="clientin",
                                options=[{"label": i, "value": i} for i in client_list],
                                value=client_list[3],
                            ),
                        ],
                    ),
                    html.Div(
                        id="select-metric-outer",
                        children=[
                            html.Label("SELECT A METRIC"),
                            dcc.Dropdown(
                                id="metric-select",
                                  options=[{"label": i, "value": i} for i in metric_list],
                                  value=metric_list[0],
                                # options=[{"label": i, "value": i} for i in cost_metric],
                                # value=cost_metric[0],
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
                             options=[{"label":i, "value": i} for i in metric_list],
                             value=[metric_list[0]],
                         ),
                     ),
                 ],
             )
        ],
    )






app.layout = html.Div(
    className="container scalable",
    children=[
            html.Div(
                id="upper-container",
                className="row",
                    children=[
                        build_upper_left_panel(),
                        build_upper_right_panel(),
                        #dash_table.DataTable(
                #            id='table',
#    columns=[{"name": i, "id": i} for i in df123.columns],
#    data=df123.to_dict('records'),
#                        )
                    ],
            ),


            html.Div(
                id="show_data",
                className='twelve columns',
                children=[
                dcc.Slider(
                    id='chartin',
                    min=1,
                    max=8,
                    marks={i: 'Week {}'.format(i) for i in range(9)},
                    value=4,
                    ),

                html.H2('Graphed Data'),
                dcc.Graph(id='Client_Output')


        ]
    )
    ],
)



#**********************************************
@app.callback(
Output(component_id='tput', component_property='children'),
[Input(component_id='inpt', component_property='value')]
)
def update_t(input_data):
    return file

#************************************************
@app.callback(
Output(component_id='Client_Output', component_property='figure'),
[Input(component_id='Client_Select', component_property='value')]
)
def buildchart(chart_data):

    #client_stuff=pd.read_csv('data/clients/kelloggs12.csv')
    file=pd.read_csv('DATA/CLIENTS/{}.csv'.format(chart_data))
    #file = pd.read_csv('data/clients/kelloggs12.csv')
    client_stuff=file[file['date']=='12/21/2020']
    #client_stuff=file[file['fips']== 1005]
    client_stuff=client_stuff.sort_values(by=['score'], ascending=False)
    client_stuff=client_stuff.head(15)

    figchart = px.bar(
        client_stuff,
        #min=1,
        #max=100,
        color="score",
        #size="score",
        hover_data=['county','state'],
        x='county',
        y='score',
        title="TAG COVID Dashboard Chart",
        range_y=[0,2],
        )

    return figchart
