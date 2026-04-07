import os
import json
from core.db_writer import write
from core.iam_control import allow
from core.central_brain import store

BASE = "/opt/aicore"
STRUCT_DB = "/opt/aicore/db/structure.jsonl"


def build_state():

    os.makedirs(BASE + "/state", exist_ok=True)

    with open(BASE + "/state/state.json", "w") as f:
        json.dump({"status": "ok"}, f)

    return True


def build_ui():

    os.makedirs(BASE + "/ui", exist_ok=True)

    with open(BASE + "/ui/dashboard.py", "w") as f:
        f.write("def dashboard(): return 'ok'")

    return True


def run(signal):

    print("\n=== STRUCTURE MANAGEMENT ===")

    raw = signal.get("raw", "").lower()

    entry = {
        "type": "STRUCTURE",
        "signal": raw,
        "status": "FAILED",
        "confidence": 0.9
    }

    if "state" in raw:
        if build_state():
            entry["name"] = "STATE_SYSTEM"
            entry["status"] = "SUCCESS"

    elif "ui" in raw:
        if build_ui():
            entry["name"] = "UI_SYSTEM"
            entry["status"] = "SUCCESS"

    # 🔴 immer lokal speichern
    write(STRUCT_DB, entry)

    # 🔴 IAM entscheidet → SoT
    if allow(entry):
        store(entry)

    return entry["status"] == "SUCCESS"
