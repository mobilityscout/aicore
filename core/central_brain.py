import json
import os
import time

DB = "/opt/aicore/db/sot.jsonl"


def store(entry):

    os.makedirs("/opt/aicore/db", exist_ok=True)

    entry["timestamp"] = time.time()

    with open(DB, "a") as f:
        f.write(json.dumps(entry) + "\n")

    print("SoT STORED:", entry)


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
