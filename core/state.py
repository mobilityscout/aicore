import json, os, time

DB = "/opt/aicore/db/state.json"

def load():
    if not os.path.exists(DB):
        return {
            "layer": 0,
            "history": [],
            "last_ok": None
        }
    return json.load(open(DB))

def save(s):
    s["t"] = time.time()
    json.dump(s, open(DB, "w"), indent=2)
