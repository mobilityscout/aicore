import requests
from core.state import load, save
from core.iam import decide
from core.guard import act
from core.layer import add, load as load_layers

def last_layer():

    layers = load_layers()
    if not layers:
        return None

    return layers[-1]

def run():

    s = load()

    prev = last_layer()

    # 🔥 SKIP LOGIK
    if prev and prev["status"] == "GREEN":
        return {
            "layer": prev["id"],
            "state": "SKIPPED",
            "status": "GREEN"
        }

    # SIGNAL
    signal = {}

    try:
        signal["tasks"] = requests.get("http://127.0.0.1:50000/tasks").status_code
    except:
        signal["tasks"] = 404

    try:
        signal["data"] = requests.get("http://127.0.0.1:50000/data").status_code
    except:
        signal["data"] = 404

    try:
        signal["state"] = requests.get("http://127.0.0.1:50000/state").status_code
    except:
        signal["state"] = 404

    # IAM
    iam = decide(signal)

    # ACT
    results = act(iam["actions"])

    # LAYER
    layer = add(iam["decision"], signal)

    s["layer"] = layer["id"]
    save(s)

    return {
        "layer": layer["id"],
        "status": layer["status"],
        "signal": signal
    }
