import json, time, os

LIB = "/opt/aicore/db/library.jsonl"


def load_library():
    if not os.path.exists(LIB):
        return []

    data = []

    with open(LIB, "r") as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except:
                continue

    return data


def store_case(signal, decision, result, action=None):

    entry = {
        "hash": signal["hash"],
        "type": signal["type"],
        "decision": decision,
        "action": action,
        "result": result,
        "status": "SOLVED" if result else "FAILED",
        "timestamp": time.time()
    }

    with open(LIB, "a") as f:
        f.write(json.dumps(entry) + "\n")


def get_failed_actions(signal_hash):

    failed = []

    if not os.path.exists(LIB):
        return failed

    with open(LIB, "r") as f:
        for line in f:
            try:
                e = json.loads(line)

                if e.get("hash") == signal_hash and e.get("status") == "FAILED":
                    failed.append(str(e.get("action")))
            except:
                continue

    return failed
