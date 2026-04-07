import json, time, os

DB = "/opt/aicore/db/library.jsonl"

def write(entry):

    entry["t"] = time.time()

    with open(DB, "a") as f:
        f.write(json.dumps(entry) + "\n")

def find(signal):

    if not os.path.exists(DB):
        return None

    for line in open(DB):
        e = json.loads(line)

        if e.get("signal") == signal:
            return e.get("action")

    return None
