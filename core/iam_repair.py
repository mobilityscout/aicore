import os, json

BASE = "/opt/aicore"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def ensure_file(path, content):

    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(content, f, indent=2)

def run():

    repaired = []

    # --- LIBRARY ---
    ensure_dir(BASE + "/library")
    ensure_dir(BASE + "/library/law")
    ensure_dir(BASE + "/library/contracts")
    ensure_dir(BASE + "/library/layers")

    # --- LAW ---
    law_path = BASE + "/library/law/law.json"

    if not os.path.exists(law_path):
        ensure_file(law_path, {
            "pipeline": [
                "VERTICAL",
                "HORIZONTAL",
                "EVALUATE",
                "GUARD",
                "IAM",
                "ACT",
                "STORE"
            ],
            "limits": {
                "max_read_mb": 10,
                "mode": "READ_ONLY_FIRST"
            }
        })
        repaired.append("LAW_CREATED")

    # --- CONTRACTS ---
    contracts = BASE + "/library/contracts/contracts.jsonl"
    if not os.path.exists(contracts):
        open(contracts, "w").close()
        repaired.append("CONTRACTS_INIT")

    # --- LAYERS ---
    layers = BASE + "/library/layers/layers.json"
    if not os.path.exists(layers):
        ensure_file(layers, [])
        repaired.append("LAYERS_INIT")

    # --- TENANTS ---
    tenants = BASE + "/tenants"
    if not os.path.exists(tenants):
        ensure_dir(tenants)
        ensure_dir(tenants + "/default")
        repaired.append("TENANT_INIT")

    return {
        "status": "REPAIRED" if repaired else "OK",
        "actions": repaired
    }
