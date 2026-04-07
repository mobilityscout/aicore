import json, time, os

STATE = "/opt/aicore/db/layer_state.json"

def next_layer():

    if not os.path.exists(STATE):
        s = {"layer": 0}
    else:
        s = json.load(open(STATE))

    s["layer"] += 1
    s["t"] = time.time()

    json.dump(s, open(STATE, "w"), indent=2)

    return s["layer"]
