import json
import time
import os
import hashlib

FILE = "/opt/aicore/audit.log"


def _hash(entry):
    return hashlib.sha256(json.dumps(entry).encode()).hexdigest()


def log(tenant, action):

    entry = {
        "tenant": tenant,
        "action": action,
        "timestamp": time.time()
    }

    entry["hash"] = _hash(entry)

    with open(FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
