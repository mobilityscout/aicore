import json, os

DB = "/opt/aicore/db"
LAYERS = DB + "/layers.jsonl"

def merge():

    if not os.path.exists(LAYERS):
        return

    lines = open(LAYERS).read().strip().split("\n")

    if len(lines) < 2:
        return

    last = json.loads(lines[-1])
    prev = json.loads(lines[-2])

    # ------------------------
    # IDENTICAL STABLE CHECK
    # ------------------------
    if last["signal"] == prev["signal"] and last["status"] == "STABLE":

        print("MERGE STABLE LAYERS → BASELINE")

        baseline = {
            "signal": last["signal"],
            "status": "BASELINE",
            "type": "MERGED"
        }

        # rewrite file (clean state)
        with open(LAYERS, "w") as f:
            f.write(json.dumps(baseline) + "\n")

        print("BASELINE CREATED:", baseline)
