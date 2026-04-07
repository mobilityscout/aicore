import json, time

DB = "/opt/aicore/library/errors.jsonl"

def log_error(error):

    entry = {
        "t": time.time(),
        "error": error,
        "status": "UNRESOLVED"
    }

    with open(DB, "a") as f:
        f.write(json.dumps(entry) + "\n")

    return entry
