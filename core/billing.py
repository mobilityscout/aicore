import json
import os
import time

FILE = "/opt/aicore/billing.json"


def log(tenant, action):

    data = []

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)

    data.append({
        "tenant": tenant,
        "action": action,
        "timestamp": time.time()
    })

    with open(FILE, "w") as f:
        json.dump(data, f)


def usage(tenant):

    if not os.path.exists(FILE):
        return 0

    with open(FILE, "r") as f:
        data = json.load(f)

    return len([x for x in data if x["tenant"] == tenant])
