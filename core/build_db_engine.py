import os
import json

DB_PATH = "/opt/aicore/db/runtime.json"

def run(action, signal):

    print("BUILD_DB → APPLY")

    os.makedirs("/opt/aicore/db", exist_ok=True)

    if not os.path.exists(DB_PATH):
        with open(DB_PATH, "w") as f:
            json.dump({"status": "initialized"}, f)

        print("DB CREATED")
        return True

    print("DB EXISTS → SKIP")
    return True
