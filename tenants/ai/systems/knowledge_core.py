import json
import os

BASE = "/opt/aicore/tenants/ai"

STAGING = BASE + "/memory_staging.json"
MASTER = BASE + "/memory_master.json"
RESTRICTED = BASE + "/memory_restricted.json"


def _load(path):
    if not os.path.exists(path):
        return {"entries": []}
    with open(path, "r") as f:
        return json.load(f)


def _save(path, data):
    with open(path, "w") as f:
        json.dump(data, f)


def store_staging(entry):
    data = _load(STAGING)
    data["entries"].append(entry)
    _save(STAGING, data)


def store_master(entry):
    data = _load(MASTER)
    data["entries"].append(entry)
    _save(MASTER, data)


def store_restricted(entry):
    data = _load(RESTRICTED)
    data["entries"].append(entry)
    _save(RESTRICTED, data)
