import time, os, json
from core.context import get_root

RUN_ID = str(int(time.time()))

TABLE = []

SCORES = {
    "L0": 10,
    "L1": 20,
    "L2": 30,
    "L3": 50,
    "L4": 70,
    "L5": 100
}

IAM = {
    "L0": "EXTERNAL",
    "L1": "INTERNAL",
    "L2": "INTERNAL",
    "L3": "INTERNAL",
    "L4": "SECURE",
    "L5": "SECURE"
}

def log_signal(layer, signal, phase):
    entry = {
        "time": time.time(),
        "run": RUN_ID,
        "layer": layer,
        "signal": signal,
        "phase": phase,
        "iam": IAM.get(layer),
        "score": SCORES.get(layer),
        "status": "OK"
    }

    TABLE.append(entry)

    # Datei schreiben
    base = get_root()
    os.makedirs(base + "/logs", exist_ok=True)

    with open(f"{base}/logs/run_{RUN_ID}.log", "a") as f:
        f.write(json.dumps(entry) + "\n")

    return entry

def get_table():
    return TABLE
