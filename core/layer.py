import json, os, time

DB = "/opt/aicore/db/layers.json"

def load():
    if not os.path.exists(DB):
        return []
    return json.load(open(DB))

def save(layers):
    json.dump(layers, open(DB, "w"), indent=2)

def classify(decision, signal):

    if decision == "OK":
        return "GREEN"

    if decision == "ERROR":
        return "RED"

    return "ORANGE"

def add(decision, signal):

    layers = load()

    status = classify(decision, signal)

    layer = {
        "id": len(layers) + 1,
        "t": time.time(),
        "decision": decision,
        "status": status,
        "signal": signal
    }

    layers.append(layer)
    save(layers)

    return layer
