import json
import os

MEMORY_FILE = "/opt/aicore/tenants/ai/brain.json"

def load():
    if not os.path.exists(MEMORY_FILE):
        return {"history": []}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f)

def store(entry):
    data = load()
    data["history"].append(entry)
    save(data)
