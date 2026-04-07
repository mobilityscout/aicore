import json
import os

FILE = "/opt/aicore/ai_learning.json"


def store(entry):

    data = []

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)

    data.append(entry)

    with open(FILE, "w") as f:
        json.dump(data, f)
