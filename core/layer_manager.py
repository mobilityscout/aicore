import json, time, os

DB = "/opt/aicore/db"
LAYERS = DB + "/layers.jsonl"

def new_layer(signal):

    entry = {
        "t": time.time(),
        "signal": signal,
        "status": "STABLE",
        "type": "AGGREGATED"
    }

    with open(LAYERS, "a") as f:
        f.write(json.dumps(entry) + "\n")

    print("LAYER STORED:", entry)
