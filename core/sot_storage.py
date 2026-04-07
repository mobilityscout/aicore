import json
import time
import os

SOT = "/opt/aicore/sot/main.jsonl"


def store(entry):

    os.makedirs("/opt/aicore/sot", exist_ok=True)

    entry["timestamp"] = time.time()

    with open(SOT, "a") as f:
        f.write(json.dumps(entry) + "\n")

    print("SoT STORED")
