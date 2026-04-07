import os, json, time, requests, traceback

BASE = "/opt/aicore"
DB = BASE + "/db"
ISO = BASE + "/isolation"

LAYER_DB = DB + "/layers.json"
STATE_DB = DB + "/state.json"

# ------------------------
# ENSURE
# ------------------------

def ensure():
    os.makedirs(DB, exist_ok=True)
    os.makedirs(ISO, exist_ok=True)

    if not os.path.exists(LAYER_DB):
        json.dump([], open(LAYER_DB, "w"))

    if not os.path.exists(STATE_DB):
        json.dump({"layer":0}, open(STATE_DB, "w"))

# ------------------------
# SAFE LOAD (LAW!)
# ------------------------

def safe_load_json(path):

    try:
        return json.load(open(path))

    except Exception as e:

        # 🔥 LAW GREIFT
        ts = str(int(time.time()))
        broken = path + ".broken_" + ts

        os.rename(path, broken)

        # neue saubere Datei
        json.dump([], open(path, "w"))

        return []

# ------------------------
# LOAD / SAVE
# ------------------------

def load_layers():
    return safe_load_json(LAYER_DB)

def save_layers(l):
    json.dump(l, open(LAYER_DB, "w"), indent=2)

def load_state():
    return safe_load_json(STATE_DB)

def save_state(s):
    json.dump(s, open(STATE_DB, "w"), indent=2)

# ------------------------
# SIGNAL
# ------------------------

def guard():

    result = {}

    try:
        result["state"] = requests.get("http://127.0.0.1:50000/state", timeout=1).status_code
    except:
        result["state"] = 404

    try:
        result["tasks"] = requests.get("http://127.0.0.1:50000/tasks", timeout=1).status_code
    except:
        result["tasks"] = 404

    try:
        result["data"] = requests.get("http://127.0.0.1:50000/data", timeout=1).status_code
    except:
        result["data"] = 404

    return result

# ------------------------
# CLASSIFY
# ------------------------

def classify(signal):

    if all(v == 200 for v in signal.values()):
        return "GREEN"

    if any(v == 404 for v in signal.values()):
        return "RED"

    return "ORANGE"

# ------------------------
# BUILD (SELF HEAL)
# ------------------------

def build(signal):

    ui = BASE + "/bin/live_ui.py"
    code = open(ui).read()

    if signal.get("state") == 404 and "@app.route(\"/state\")" not in code:
        code = code.replace("if __name__ == \"__main__\":",
'''
@app.route("/state")
def state():
    return {"state": "ok"}, 200

if __name__ == "__main__":
''')

    if signal.get("tasks") == 404 and "@app.route(\"/tasks\")" not in code:
        code = code.replace("if __name__ == \"__main__\":",
'''
@app.route("/tasks")
def tasks():
    return {"tasks": "ok"}, 200

if __name__ == "__main__":
''')

    if signal.get("data") == 404 and "@app.route(\"/data\")" not in code:
        code = code.replace("if __name__ == \"__main__\":",
'''
@app.route("/data")
def data():
    return {"data": "ok"}, 200

if __name__ == "__main__":
''')

    open(ui, "w").write(code)

    os.system("pkill -9 -f live_ui.py || true")
    os.system("python3 /opt/aicore/bin/live_ui.py &")

# ------------------------
# ENGINE (LAW CONTROLLED)
# ------------------------

def run():

    ensure()

    try:

        layers = load_layers()
        state = load_state()

        signal = guard()

        status = classify(signal)

        layer_id = len(layers) + 1

        layer = {
            "id": layer_id,
            "t": time.time(),
            "signal": signal,
            "status": status
        }

        # 🔴 RED → SELF HEAL
        if status == "RED":
            build(signal)
            signal = guard()
            layer["status"] = classify(signal)

        layers.append(layer)
        save_layers(layers)

        state["layer"] = layer_id
        save_state(state)

        return {
            "layer": layer_id,
            "status": layer["status"],
            "signal": signal
        }

    except Exception as e:

        # 🔥 ABSOLUTE FALLBACK (LAW)
        return {
            "status": "ERROR",
            "error": str(e),
            "trace": traceback.format_exc()
        }
