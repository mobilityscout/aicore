import json, time, os

LAYER_DB = "/opt/aicore/db/layers.jsonl"

def create_layer(signal, decision, result):
    layer = {
        "id": str(int(time.time()*1000)),
        "signal_hash": signal["hash"],
        "decision": decision,
        "result": result,
        "state": "GREEN" if result else "RED"
    }

    with open(LAYER_DB, "a") as f:
        f.write(json.dumps(layer) + "\n")

    return layer
