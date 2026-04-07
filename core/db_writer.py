import json
import time


def write(path, entry):

    entry["timestamp"] = time.time()

    with open(path, "a") as f:
        f.write(json.dumps(entry) + "\n")
