import json, os, time

LIB = "/opt/aicore/db/library.jsonl"

# ------------------------
# KNOWLEDGE LOOKUP
# ------------------------

def find_known(signal):

    if not os.path.exists(LIB):
        return None

    for line in open(LIB):
        try:
            e = json.loads(line)
            if e.get("signal") == signal:
                return e.get("actions")
        except:
            continue

    return None

# ------------------------
# DECISION ENGINE
# ------------------------

def decide(layer):

    signal = layer.get("signal")
    failed = layer.get("failed")

    # 1. KNOWLEDGE
    known = find_known(signal)
    if known:
        return {
            "decision": "FIX",
            "actions": known,
            "reason": "KNOWN_PATTERN"
        }

    # 2. STANDARD FIX (lokal)
    if failed in ["state", "tasks", "data"]:
        return {
            "decision": "FIX",
            "actions": [f"BUILD_{failed.upper()}"],
            "reason": "LOCAL_FIX"
        }

    # 3. UNKNOWN → ESCALATE
    return {
        "decision": "ESCALATE",
        "actions": [],
        "reason": "UNKNOWN_SIGNAL"
    }
