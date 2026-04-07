import requests

def run(action):

    print("GUARD VERIFY:", action["type"])

    if action["type"] == "ADD_ENDPOINT":
        return check_endpoint("/state")

    if action["type"] == "INSTALL_PACKAGE":
        return check_import(action.get("name"))

    return False


def check_endpoint(path):
    try:
        r = requests.get("http://127.0.0.1:50000" + path, timeout=2)
        return r.status_code == 200
    except:
        return False


def check_import(pkg):
    try:
        __import__(pkg)
        return True
    except:
        return False
