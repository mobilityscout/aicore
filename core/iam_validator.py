import os
from core.iam_repair import run as repair

BASE = "/opt/aicore"

def exists(p):
    return os.path.exists(p)

def validate():

    result = {
        "law": exists(BASE + "/library/law/law.json"),
        "contracts": exists(BASE + "/library/contracts/contracts.jsonl"),
        "layers": exists(BASE + "/library/layers/layers.json"),
        "tenants": exists(BASE + "/tenants"),
    }

    if all(result.values()):
        return {"status": "STABLE", "details": result}

    # --- SELF REPAIR ---
    fix = repair()

    # --- RECHECK ---
    result = {
        "law": exists(BASE + "/library/law/law.json"),
        "contracts": exists(BASE + "/library/contracts/contracts.jsonl"),
        "layers": exists(BASE + "/library/layers/layers.json"),
        "tenants": exists(BASE + "/tenants"),
    }

    if all(result.values()):
        return {
            "status": "RECOVERED",
            "repair": fix,
            "details": result
        }

    return {
        "status": "BROKEN",
        "repair": fix,
        "details": result
    }
