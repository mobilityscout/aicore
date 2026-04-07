import os, json, time

BASE = "/opt/aicore/db"
os.makedirs(BASE, exist_ok=True)

SHORT = BASE + "/short.json"
MID   = BASE + "/mid.jsonl"
LONG  = BASE + "/long.jsonl"

def write_short(signal):
    json.dump({"t": time.time(), "signal": signal}, open(SHORT, "w"), indent=2)

def read_short():
    if not os.path.exists(SHORT):
        return None
    try:
        return json.load(open(SHORT))
    except:
        return None

def write_mid(entry):
    with open(MID, "a") as f:
        f.write(json.dumps(entry) + "\n")

# 🔥 WICHTIG: FILTER NUR SOLVED
def find_solution(signal):

    if not os.path.exists(LONG):
        return None

    for line in open(LONG):
        try:
            e = json.loads(line)
            if e.get("signal") == signal and e.get("status") == "SOLVED":
                return e
        except:
            continue

    return None

def write_long(entry):
    with open(LONG, "a") as f:
        f.write(json.dumps(entry) + "\n")
