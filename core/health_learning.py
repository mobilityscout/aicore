import json
import os

DB = "/opt/aicore/db/health_learning.jsonl"


def load():

    if not os.path.exists(DB):
        return []

    data = []

    for line in open(DB):
        try:
            data.append(json.loads(line))
        except:
            continue

    return data


def store(error_type, fix_action):

    entry = {
        "error": error_type,
        "fix": fix_action
    }

    with open(DB, "a") as f:
        f.write(json.dumps(entry) + "\n")


def find(error_type):

    data = load()

    for d in data:
        if d["error"] == error_type:
            return d["fix"]

    return None
