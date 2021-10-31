# RICHARD CASTRO
# AUGUST 28, 2020
# DASHBOARD


# IMPORT dependency FILES
from LIBRARIES import *
from CARDS import *
########################


# SETTING UP CLIENT DICTIONARY ARRAY TO HOLD THE CLIENT LOCATIONS
client_dict = {}


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=443, ssl_context=('cert.pem', 'key.pem'))
