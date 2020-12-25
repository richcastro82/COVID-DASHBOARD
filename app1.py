from LIBRARIES import *
import plotly.graph_objects as go

client_list = ['KELLOGGS', 'PEPSI', 'A&W', 'US FOODS']
metric_list = ['CASES', 'DEATHS', 'ACTIVE', 'RT', 'CR', 'MOB', 'TPR']

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
df_PEPSI = pd.read_csv(DATA_PATH.joinpath("PEPSI.csv"))
df_KELLOGGS = pd.read_csv(DATA_PATH.joinpath("KELLOGGS.csv"))
df_AW = pd.read_csv(DATA_PATH.joinpath("A&W.csv"))



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
        id="upper-left",
        className="six columns",
        children=[
            html.P(
                className="section-title",
                children="Choose CLIENT Locations",
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
#                    html.Div(
#                        id="select-metric-outer",
#                        children=[
#                            html.Label("SELECT A METRIC"),
#                            dcc.Dropdown(
#                                id="metric-select",
#                                  options=[{"label": i, "value": i} for i in metric_list],
#                                  value=metric_list[0],
#                                # options=[{"label": i, "value": i} for i in cost_metric],
#                                # value=cost_metric[0],
#                            ),
#                        ],
#                    ),
                ],
            ),

             html.Div(
                 id="region-select-outer",
                 className="control-row-2",
                 children=[
                     html.Label("Pick a Region"),
                     html.Div(
                         id="checklist-container",
                         children=dcc.Checklist(
                             id="region-select-all",
                             options=[{"label": "Select All Regions", "value": "All"}],
                             value=[],
                         ),
                     ),
                     html.Div(
                        id="region-select-dropdown-outer",
                        children=dcc.Dropdown(
                             id="region-select", multi=True, searchable=True,
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
                        build_upper_left_panel()
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


                dcc.Graph(id='chartout')

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
Output(component_id='chartout', component_property='figure'),
[Input(component_id='chartin', component_property='value')]
)
def buildchart(chart_data):

    file1=pd.read_csv('data/data.csv')

    figchart = px.scatter(
        file1,
         #min=0,
         #max=100,
        color="weekly change",
        size="population",
        hover_data=['county'],
        x="date",
        y="score",
        title="TAG COVID Dashboard Chart"
        )

    return figchart
