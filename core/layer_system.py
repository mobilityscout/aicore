import json, time, os

DB = "/opt/aicore/db"
STATE = DB + "/layer_state.json"
LOG = DB + "/layer_log.jsonl"

os.makedirs(DB, exist_ok=True)

def next_layer():

    if not os.path.exists(STATE):
        s = {"layer": 0}
    else:
        s = json.load(open(STATE))

    s["layer"] += 1
    s["t"] = time.time()

    json.dump(s, open(STATE, "w"), indent=2)

    return s["layer"]

def score(signal):

    total = len(signal)
    ok = sum(1 for v in signal.values() if v == 200)
    fail = total - ok

    status = "GREEN" if fail == 0 else "RED"

    return {
        "ok": ok,
        "fail": fail,
        "total": total,
        "status": status,
        "score": round(ok / total, 2)
    }

def log(layer, signal, result):

    entry = {
        "t": time.time(),
        "layer": layer,
        "signal": signal,
        "result": result
    }

    with open(LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")
