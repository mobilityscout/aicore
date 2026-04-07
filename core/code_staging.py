import json
import os

FILE = "/opt/aicore/code_staging.json"

def store(entry):

    data = []

    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                data = json.load(f)
        except:
            data = []

    data.append(entry)

    with open(FILE, "w") as f:
        json.dump(data, f)
