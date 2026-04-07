import json, os, time

TASKS_FILE = "/opt/aicore/tenants/ms24/ai-platform/storage/tasks.json"

DEFAULT = {
    "current": "INIT",
    "next": "SCAN",
    "done": []
}

def load():
    if not os.path.exists(TASKS_FILE):
        save(DEFAULT)
    return json.load(open(TASKS_FILE))

def save(data):
    with open(TASKS_FILE,"w") as f:
        json.dump(data,f)

def step(new_task):
    t = load()
    t["done"].append(t["current"])
    t["current"] = new_task
    t["next"] = "NEXT_UNKNOWN"
    save(t)
