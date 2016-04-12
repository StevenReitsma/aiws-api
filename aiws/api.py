import requests
import json

HOSTNAME = "home.properchaos.nl"
PORT = "80"
SERVER = "http://"+HOSTNAME+":"+PORT



TEAM_PASSWORD = ""
TEAM_NAME = ""

def authenticate(name, password):
    global TEAM_PASSWORD
    TEAM_PASSWORD = password
    global TEAM_NAME
    TEAM_NAME = name

def validate_credentials(*args):
    if TEAM_PASSWORD == "" or TEAM_NAME == "":
        raise Exception('Team name or password is not set, please call api.authenticate first.')

def get_context(run_id, request_number):
    validate_credentials()

    if run_id < 0:
        raise ValueError("run_id has an invalid value of {}".format(run_id))

    if request_number < 0 or request_number > 9999:
        raise ValueError("request_number has an invalid value of {}".format(request_number))

    params = {"team_id": TEAM_NAME,
        "team_password": TEAM_PASSWORD,
        "run_id": run_id,
        "request_number": request_number
    }

    r = requests.get(SERVER+"/get_context", params=params)
    
    dict_response = json.decode(r)
    return dict_response


if __name__ == "__main__":
    authenticate("test","test")
    print get_context(4,5)
