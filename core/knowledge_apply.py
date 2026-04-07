import json, os

LIB = "/opt/aicore/db/library.jsonl"

def find_solution(signal):

    if not os.path.exists(LIB):
        return None

    for line in open(LIB):
        try:
            e = json.loads(line)
            if e.get("signal") == signal:
                return e.get("action")
        except:
            continue

    return None

def store_solution(signal, action):

    entry = {
        "signal": signal,
        "action": action
    }

    with open(LIB, "a") as f:
        f.write(json.dumps(entry) + "\n")
