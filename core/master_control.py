import json
from tenants.ai.systems.knowledge_core import store_master

STAGING = "/opt/aicore/tenants/ai/memory_staging.json"


def approve(index):

    with open(STAGING, "r") as f:
        data = json.load(f)

    entry = data["entries"][index]

    entry["approved"] = True

    store_master(entry)

    print("APPROVED:", entry)
