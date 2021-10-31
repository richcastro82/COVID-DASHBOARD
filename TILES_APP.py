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
Location_List=[]
Chart_List=['Map', 'Bar', 'Line', 'Scatter']

for i in Directory.clients:
    Client_List.append('{}'.format(i))

for i in Directory.metrics:
    Metrics_List.append('{}'.format(i))

for i in Directory.locations:
    Location_List.append('{}'.format(i))

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




scores=[]
st=[]
employ=[]
popu=[]
facilities=[]
def build_tiles():
    df=pd.read_csv('DATA\Client_Locations/Kelloggs.csv')
    for index, rows in df.iterrows():
        county=(rows.county)
        facilities.append(county)
        pop=(rows.metrics)
        popu.append(pop)
        employeeCount=(rows.employeeCount)
        employ.append(employeeCount)
        state=(rows.state)
        st.append(state)
        score=(rows.score)
        scores.append(score)





def make_divs(facilities, scores, st, popu):
    count=0
    df=pd.read_csv('DATA\Client_Locations/Kelloggs.csv')
    for index, i in df.iterrows():
        count+=1

    i=0
    return_Divs=[]
    while i < count:
        return_Divs.append(
        html.Div('Facility:{} at position: {}'.format(facilities[i], i)))
        i+=1
        print(return_Divs)
    return return_Divs






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



#=========================================================================================
# THIS SECTION IS FOR THE TABLE THAT DISPLAYS TO DATA UNDER THE CHART
# READ IN A CLIENT LOCATION FILE BASED ON THE USER INPUT
#Client_Select=Client_List[1]
#Client_File=pd.read_csv('data/client_locations/{}.csv'.format(Client_Select.value))
#df=Client_File.drop(['fips', 'country', 'lat', 'long'], axis=1)


#==================================================================
#========== HTML & CSS CODE ====================================
#==========================================================
app.layout = html.Div(
    className="container scalable",
    children=[
        html.Div(
        className="client-tile",
        children=[
        build_tiles(),
        make_divs(facilities, scores, st, popu)

        ]
        )

])
